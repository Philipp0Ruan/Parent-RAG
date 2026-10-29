"""Parent RAG com busca nos filhos e contexto dos pais."""

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path

from rag_base import Config, RAIZ, RAGBase, dividir_trechos


@dataclass(frozen=True)
class ParentConfig(Config):
    parent_tokens: int = 1000
    parent_overlap_tokens: int = 100
    child_top_k: int = 16

    def __post_init__(self):
        super().__post_init__()
        if not 0 <= self.parent_overlap_tokens < self.parent_tokens or self.parent_tokens <= self.chunk_tokens:
            raise ValueError("Os pais devem ser maiores que os filhos, com sobreposição válida.")
        if self.child_top_k < self.top_k:
            raise ValueError("child_top_k deve ser maior ou igual a top_k.")

    def assinatura(self):
        dados = [super().assinatura(), self.parent_tokens, self.parent_overlap_tokens]
        return hashlib.sha256(json.dumps(dados).encode()).hexdigest()


class ParentRAG(RAGBase):
    abordagem = "parent"

    def __init__(self, root: Path = RAIZ, config: ParentConfig | None = None):
        super().__init__(root, config or ParentConfig.carregar(root))
        self.pais = {}

    def dividir_documentos(self, paginas):
        pais = dividir_trechos(paginas, self.modelo.tokenizer, self.config,
                              tamanho=self.config.parent_tokens,
                              sobreposicao=self.config.parent_overlap_tokens)
        self.pais = {pai["id"]: pai for pai in pais}
        filhos = []
        for pai in pais:
            for filho in dividir_trechos([pai], self.modelo.tokenizer, self.config):
                filho["parent_id"] = pai["id"]
                filho["id"] = pai["id"] + "-" + filho["id"]
                filhos.append(filho)
        return filhos

    def extras_indice(self):
        return {"pais": self.pais}

    def carregar_extras(self, extras):
        self.pais = extras.get("pais", {})
        if not self.pais or any(f.get("parent_id") not in self.pais for f in self.trechos):
            raise ValueError("Relação entre pais e filhos inválida. Reconstrua o índice.")

    def buscar(self, pergunta, top_k=None):
        k = self.config.top_k if top_k is None else top_k
        if k < 1:
            raise ValueError("top_k deve ser positivo.")
        filhos = super().buscar(pergunta, self.config.child_top_k)
        encontrados = {}
        for filho in filhos:
            identificador = filho["parent_id"]
            if identificador not in encontrados:
                encontrados[identificador] = {**self.pais[identificador],
                                              "similarity": filho["similarity"], "child_hits": []}
            encontrados[identificador]["child_hits"].append(
                {"id": filho["id"], "similarity": filho["similarity"]})
        resultado = list(encontrados.values())[:k]
        self.ultima_busca = {"filhos_recuperados": len(filhos),
                             "pais_unicos": len(encontrados),
                             "pais_selecionados": [p["id"] for p in resultado]}
        return resultado


if __name__ == "__main__":
    from cli import executar
    raise SystemExit(executar(ParentRAG))
