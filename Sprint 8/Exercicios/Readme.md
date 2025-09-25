# Exercícios

## Objetivo
Os exercícios desta sprint foram projetados para introduzir o uso de PySpark e Python em problemas de manipulação e geração de dados em grande escala.

## Exercício 1: Geração de Nomes Aleatórios
- **Descrição**: Um script Python foi desenvolvido para gerar um arquivo de texto com 10 milhões de nomes aleatórios, escolhidos a partir de 3.000 nomes únicos. 
- **Propósito**: Simular um grande conjunto de dados para praticar a manipulação em PySpark.
- **Arquivo**: [Exercicio](../Exercicios/Exercicio_geração/Exercicio%20real/)

### Resumo do Código
- Usa o módulo `random` para escolher aleatoriamente nomes.
- Gera um arquivo chamado `nomes_aleatorios.txt` com 10 milhões de linhas.
- Estrutura básica:
  1. Cria uma lista de nomes únicos com o módulo `names`.
  2. Seleciona nomes aleatoriamente e escreve em arquivo. 



## Exercício 2: Manipulação com PySpark
- **Descrição**: Um notebook em PySpark foi usado para realizar as seguintes operações:
    - Carregar o arquivo gerado no Exercício 1.
    - Limpeza e transformação dos dados.
    - Operações como contagem de frequência e agrupamento. 

[Execicio](../Exercicios/Exercicio_Spark/Exercicios_Intro.ipynb)