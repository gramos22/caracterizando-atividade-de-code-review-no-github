# LAB03: Caracterizando a Atividade de Code Review no GitHub

## Visão Geral

Este repositório contém o código e a documentação para o Laboratório 03 do curso de Engenharia de Software, focado na experimentação de software. O objetivo principal é analisar a atividade de code review em repositórios populares do GitHub, identificando variáveis que influenciam o merge de um Pull Request (PR).  Analisaremos dados de PRs submetidos aos 200 repositórios Java mais populares, garantindo que cada repositório tenha pelo menos 100 PRs (merged + closed).

## Questões de Pesquisa

Este laboratório busca responder às seguintes questões de pesquisa, divididas em duas dimensões:

**A. Feedback Final das Revisões (Status do PR):**

*   **RQ 01:** Qual a relação entre o tamanho dos PRs e o feedback final das revisões?
*   **RQ 02:** Qual a relação entre o tempo de análise dos PRs e o feedback final das revisões?
*   **RQ 03:** Qual a relação entre a descrição dos PRs e o feedback final das revisões?
*   **RQ 04:** Qual a relação entre as interações nos PRs e o feedback final das revisões?

**B. Número de Revisões:**

*   **RQ 05:** Qual a relação entre o tamanho dos PRs e o número de revisões realizadas?
*   **RQ 06:** Qual a relação entre o tempo de análise dos PRs e o número de revisões realizadas?
*   **RQ 07:** Qual a relação entre a descrição dos PRs e o número de revisões realizadas?
*   **RQ 08:** Qual a relação entre as interações nos PRs e o número de revisões realizadas?

## Métricas

As seguintes métricas serão utilizadas para responder às questões de pesquisa:

**Métricas de Tamanho:**

*   **Número de Arquivos:** Quantidade de arquivos modificados no PR.
*   **Linhas Adicionadas e Removidas:** Total de linhas de código adicionadas e removidas.

**Métricas de Tempo:**

*   **Tempo de Análise:** Intervalo entre a criação do PR e a última atividade (fechamento ou merge).

**Métricas de Descrição:**

*   **Descrição:** Número de caracteres no corpo da descrição do PR (em Markdown).

**Métricas de Interação:**

*   **Número de Participantes:** Quantidade de usuários envolvidos na revisão do PR.
*   **Número de Comentários:** Quantidade de comentários trocados durante a revisão.

## Metodologia

1.  **Criação do Dataset:**
    *   Identificar os 200 repositórios Java mais populares no GitHub.
    *   Selecionar PRs de cada repositório que possuam pelo menos 100 PRs (merged + closed).
    *   Filtrar PRs que passaram pelo processo de code review (status MERGED ou CLOSED) e que possuam pelo menos uma revisão.
    *   Remover PRs revisados automaticamente (por bots ou CI/CD) com tempo de revisão menor que uma hora.

2.  **Análise de Dados:**
    *   Coletar as métricas definidas acima para cada PR no dataset.
    *   Analisar as relações entre as métricas utilizando testes estatísticos (Spearman ou Pearson - a escolha será justificada no relatório).

## Processo de Desenvolvimento

O processo de desenvolvimento será dividido em três etapas:

*   **Lab03S01:** Criação da lista de repositórios selecionados e desenvolvimento de um script para coletar os PRs e as métricas definidas.
*   **Lab03S02:** Criação do dataset completo com os valores de todas as métricas necessárias e elaboração da primeira versão do relatório final, incluindo as hipóteses iniciais.
*   **Lab03S03:** Análise e visualização dos dados e elaboração do relatório final.

## Setup

*   **Linguagem:** Python (detalhes sobre as bibliotecas utilizadas serão adicionados posteriormente)
*   **API:** GitHub GraphQL API
*   **Ferramentas:** (A lista de ferramentas específicas será adicionada conforme o desenvolvimento)

## Bônus

A análise das correlações será aprofundada utilizando um teste estatístico apropriado (Spearman ou Pearson), e gráficos de correlação serão gerados para visualizar o comportamento dos dados. A justificativa para a escolha do teste estatístico será incluída no relatório.

## Contributing

Este projeto é desenvolvido por [Gabriel Ramos Ferreira](https://github.com/gramos22/) e [João Pedro Braga](https://github.com/joaopedro-braga). Contribuições são bem-vindas, mas por favor, entre em contato conosco antes de propor mudanças significativas.

## Referências

*   [Link para o cronograma do laboratório](https://github.com/joaopauloaramuni/laboratorio-de-experimentacao-de-software/tree/main/CRONOGRAMA)
