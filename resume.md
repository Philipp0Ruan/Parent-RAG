# Resumo de desenvolvimento — Parent RAG

Atualizado em 29/10/2026.

## Objetivo

Responder às cinco perguntas sobre Os Sertões buscando trechos filhos e recuperando os blocos pais correspondentes para fornecer contexto ao LLM.

Repositório: https://github.com/Philipp0Ruan/Parent-RAG

Este projeto tem seu próprio código, notebook, dados, resultados e checklist. Pode ser desenvolvido e executado dentro desta pasta, sem importar código de outro repositório.

## Situação atual

A preparação inicial está concluída. O arquivo Python apresenta o roteiro e lê as cinco perguntas; o notebook importa essa base e também lê as perguntas. A recuperação, a geração com LLM e a avaliação final ainda precisam ser implementadas. Ainda não há respostas geradas nem resultados do experimento.

## Arquivos para continuar o trabalho

- [parent_rag.py](parent_rag.py): base Python da implementação.
- [notebooks/parent_rag.ipynb](notebooks/parent_rag.ipynb): execução das etapas no Jupyter.
- [evaluation/perguntas.json](evaluation/perguntas.json): perguntas Q1 a Q5.
- [CHECKLIST_EXECUCAO.md](CHECKLIST_EXECUCAO.md): controle local detalhado das tarefas, ignorado pelo Git.
- [README.md](README.md): apresentação do projeto e instruções de uso.
- `data/`: PDF e dados extraídos, mantidos localmente.
- `storage/`: índices e dados persistidos, a criar durante a implementação.
- `results/`: respostas e avaliações, a produzir durante a execução.

## Fluxo desta abordagem

```text
PDF → blocos pais → trechos filhos → embeddings dos filhos → busca → recuperação dos pais → contexto → resposta com fontes
```

A busca deve operar sobre os filhos; o LLM deve receber os pais correspondentes, sem pais repetidos e com as páginas preservadas.

## Etapas para concluir

1. Definir o ambiente, as dependências, o modelo de embeddings e o LLM neste repositório.
2. Baixar o livro, registrar o hash, extrair o texto por página e conferir a limpeza.
3. Criar blocos pais e trechos filhos, com parent_id, child_id, fonte e páginas.
4. Indexar os embeddings dos filhos e armazenar os pais para consulta por identificador.
5. Buscar filhos, recuperar seus pais, remover pais duplicados e limitar o contexto.
6. Gerar respostas em português com páginas e indicação de evidência insuficiente.
7. Executar as cinco perguntas e verificar a relação entre filhos encontrados e pais usados.
8. Validar persistência e recarga, executar Python e notebook e documentar os resultados.

## Próximo passo

Começar pela seção **1. Ambiente e escolhas** do checklist. Definir bibliotecas, modelos e configuração antes de implementar a leitura e a recuperação do livro. O Python 3.12 já foi usado na verificação inicial; o ambiente virtual, as dependências de RAG e a instalação do Jupyter ainda precisam ser preparados.

Manter as funções na base Python e usá-las no notebook, com os mesmos parâmetros, para que os dois formatos produzam resultados equivalentes.

## Perguntas que precisam ser respondidas

- **Q1:** Qual é a visão de Euclides da Cunha sobre o ambiente natural do sertão nordestino e como ele influencia a vida dos habitantes?
- **Q2:** Quais são as principais características da população sertaneja descritas por Euclides da Cunha? Como ele relaciona essas características com o ambiente em que vivem?
- **Q3:** Qual foi o contexto histórico e político que levou à Guerra de Canudos, segundo Euclides da Cunha?
- **Q4:** Como Euclides da Cunha descreve a figura de Antônio Conselheiro e seu papel na Guerra de Canudos?
- **Q5:** Quais são os principais aspectos da crítica social e política presentes em "Os Sertões"? Como esses aspectos refletem a visão do autor sobre o Brasil da época?

## Critérios de conclusão

O projeto estará concluído quando o Python e o notebook executarem o pipeline completo, as cinco respostas estiverem registradas com trechos e páginas verificáveis, o índice puder ser recarregado e o README explicar uma execução reproduzível.

Registrar configurações, tempos e tokens/custo quando disponíveis. Apontar evidências insuficientes e limitações. Separar o texto de Euclides dos materiais editoriais do PDF e distinguir a página física do PDF da página impressa.

Uma comparação futura poderá usar os resultados dos outros experimentos. Isso não exige uma pasta de projeto geral nem dependências entre os repositórios.

## Fonte do livro

[PDF de Os Sertões](https://fundar.org.br/wp-content/uploads/2021/06/os-sertoes.pdf).

Ao terminar cada etapa, atualizar este resumo com a situação real e marcar no checklist apenas o que tiver sido verificado.
