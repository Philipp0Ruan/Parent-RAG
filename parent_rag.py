"""Preparação do Parent RAG para o desafio com Os Sertões.

Este arquivo guarda o roteiro e lê as perguntas locais. A recuperação e a
geração serão implementadas nas próximas etapas. O notebook importa esta base.
"""

from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
TITULO = 'Parent RAG'
STATUS = "Preparação inicial: o pipeline RAG ainda será implementado."

# As etapas seguem a mesma ordem do notebook.
ROTEIRO: tuple[tuple[str, str], ...] = (
    ('1. Ambiente e configuração',
     'Definir e instalar as dependências, selecionar modelos, carregar variáveis de ambiente e registrar versões e parâmetros. Não inserir chaves no notebook.'),
    ('2. PDF e corpus',
     'Baixar o PDF para `data/os-sertoes.pdf`, registrar seu hash e extrair o texto com fonte e páginas. Conferir a limpeza e separar os textos editoriais do corpus da obra.\n\nA execução deve localizar a raiz do repositório independentemente da pasta em que o Jupyter foi aberto.'),
    ('3. Criar pais e filhos',
     'A implementar: Dividir o texto em blocos maiores e subdividir cada bloco em trechos menores, com parent_id, child_id, fonte e páginas.'),
    ('4. Indexar e armazenar',
     'A implementar: Gerar embeddings apenas dos filhos e guardar os pais em um armazenamento consultável por parent_id.'),
    ('5. Recuperar o contexto',
     'A implementar: Buscar os filhos, resolver seus parent_ids, remover pais duplicados preservando a ordem de relevância e limitar o contexto sem perder a ligação com as páginas.'),
    ('6. Prompt e geração',
     'Montar o contexto com fontes e páginas. Responder em português, distinguir interpretações do autor de fatos atuais e indicar quando faltarem evidências. Usar o mesmo prompt base na comparação entre abordagens.'),
    ('7. Perguntas do desafio',
     'Carregar `evaluation/perguntas.json` e executar as cinco perguntas, preservando os identificadores.\n\n- **Q1:** Qual é a visão de Euclides da Cunha sobre o ambiente natural do sertão nordestino e como ele influencia a vida dos habitantes?\n- **Q2:** Quais são as principais características da população sertaneja descritas por Euclides da Cunha? Como ele relaciona essas características com o ambiente em que vivem?\n- **Q3:** Qual foi o contexto histórico e político que levou à Guerra de Canudos, segundo Euclides da Cunha?\n- **Q4:** Como Euclides da Cunha descreve a figura de Antônio Conselheiro e seu papel na Guerra de Canudos?\n- **Q5:** Quais são os principais aspectos da crítica social e política presentes em "Os Sertões"? Como esses aspectos refletem a visão do autor sobre o Brasil da época?'),
    ('8. Avaliação e resultados',
     'A consulta deve buscar os filhos e entregar seus pais ao modelo, com a relação entre os dois visível no notebook e sem repetir o mesmo pai no contexto.\n\nGuardar respostas, evidências, páginas, parâmetros, latência e uso de tokens quando disponível em `results/`. Conferir manualmente a sustentação das respostas no PDF.\n\nVamos comparar com o Naive RAG para verificar se o contexto mais amplo ajuda nas perguntas interpretativas e quanto aumenta o consumo de contexto.'),
    ('9. Reprodução e conclusão',
     'Reiniciar o kernel, executar todas as células em ordem e validar a recarga do índice. Documentar instalação e execução no README somente depois de verificar o fluxo completo. Registrar resultados reais e limitações.'),
)


def carregar_perguntas() -> list[dict[str, str]]:
    """Lê as cinco perguntas, independentemente da pasta de execução."""
    caminho = RAIZ / "evaluation" / "perguntas.json"
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    return dados["perguntas"]


def mostrar_preparacao() -> None:
    """Mostra o andamento e o roteiro, sem executar o pipeline futuro."""
    print(f"{TITULO} — Os Sertões")
    print(STATUS)
    print("\nEtapas:")
    for titulo, _ in ROTEIRO:
        print(f"  {titulo}")
    print("\nPerguntas do desafio:")
    for item in carregar_perguntas():
        print(f"  {item['id']}: {item['pergunta']}")


if __name__ == "__main__":
    mostrar_preparacao()
