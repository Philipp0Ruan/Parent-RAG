# Parent RAG — Os Sertões

Este projeto vai responder perguntas sobre **Os Sertões** buscando trechos curtos e recuperando os blocos maiores aos quais eles pertencem. A proposta é localizar informações específicas sem perder o contexto necessário para interpretar o texto.

Faz parte do Desafio RAG, com três abordagens em repositórios separados:
[Naive RAG](https://github.com/Philipp0Ruan/Naive-RAG),
[Parent RAG](https://github.com/Philipp0Ruan/Parent-RAG) e
[Rerank RAG](https://github.com/Philipp0Ruan/Rerank-RAG).

## Situação atual

A estrutura inicial está pronta. O notebook contém o roteiro de desenvolvimento; a leitura do PDF, a recuperação e a geração das respostas ainda serão implementadas. Ainda não há respostas geradas nem resultados de avaliação.

## Como vai funcionar

```text
PDF → blocos pais → trechos filhos → embeddings dos filhos → busca → recuperação dos pais → resposta com fontes
```

- **Criar pais e filhos:** Dividir o texto em blocos maiores e subdividir cada bloco em trechos menores, com parent_id, child_id, fonte e páginas.
- **Indexar e armazenar:** Gerar embeddings apenas dos filhos e guardar os pais em um armazenamento consultável por parent_id.
- **Recuperar o contexto:** Buscar os filhos, resolver seus parent_ids, remover pais duplicados preservando a ordem de relevância e limitar o contexto sem perder a ligação com as páginas.

Vamos comparar com o Naive RAG para verificar se o contexto mais amplo ajuda nas perguntas interpretativas e quanto aumenta o consumo de contexto.

## Perguntas do desafio

1. Qual é a visão de Euclides da Cunha sobre o ambiente natural do sertão nordestino e como ele influencia a vida dos habitantes?
2. Quais são as principais características da população sertaneja descritas por Euclides da Cunha? Como ele relaciona essas características com o ambiente em que vivem?
3. Qual foi o contexto histórico e político que levou à Guerra de Canudos, segundo Euclides da Cunha?
4. Como Euclides da Cunha descreve a figura de Antônio Conselheiro e seu papel na Guerra de Canudos?
5. Quais são os principais aspectos da crítica social e política presentes em "Os Sertões"? Como esses aspectos refletem a visão do autor sobre o Brasil da época?

As perguntas também estão em [evaluation/perguntas.json](evaluation/perguntas.json), com identificadores iguais nos três projetos.

## Organização

```text
notebooks/parent_rag.ipynb   # roteiro do experimento
evaluation/perguntas.json     # cinco perguntas do desafio
data/                        # PDF e dados extraídos, somente locais
results/                     # respostas e avaliações, quando forem geradas
```

O notebook fica em [notebooks/parent_rag.ipynb](notebooks/parent_rag.ipynb).

## Desenvolvimento e execução

Vamos implementar o notebook por etapas: preparar o ambiente, carregar e conferir o livro, construir a recuperação, gerar as respostas e avaliar as evidências.

Python e Jupyter serão usados para o experimento. O provedor do LLM, os modelos, as bibliotecas e suas versões serão definidos na implementação. As instruções de instalação e execução serão adicionadas aqui depois de validadas. Por enquanto, o notebook é um roteiro e não executa um pipeline RAG.

## Como avaliar

A consulta deve buscar os filhos e entregar seus pais ao modelo, com a relação entre os dois visível no notebook e sem repetir o mesmo pai no contexto.

Para cada pergunta, vamos guardar a resposta, os trechos utilizados, as páginas, os parâmetros e o tempo de execução. A revisão vai conferir se a resposta atende à pergunta e se as fontes sustentam o que o modelo escreveu. Afirmações sem evidência devem ser identificadas, e o modelo deve indicar quando o contexto for insuficiente.

Na comparação entre os projetos, vamos manter o mesmo PDF, as mesmas perguntas e, sempre que possível, o mesmo modelo de geração, embeddings, prompt e limite de contexto. As diferenças de configuração serão registradas junto dos resultados.

## Material de referência

- [PDF de Os Sertões disponibilizado pela Fundar](https://fundar.org.br/wp-content/uploads/2021/06/os-sertoes.pdf).
- [Solução de referência da Rocketseat](https://github.com/rocketseat-education/ia-para-devs/tree/master/Desafio%20RAG).

O PDF será salvo localmente em `data/os-sertoes.pdf`. A edição inclui material editorial; vamos separar esse conteúdo do texto de Euclides antes de avaliar as respostas e distinguir o número da página no PDF da numeração impressa no livro.
