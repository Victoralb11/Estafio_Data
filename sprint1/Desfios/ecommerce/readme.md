# Desafio 
Neste desafio, nos foi pedido para manipularmos um arquivo .csv, no qual conteria alguns itens que foram vendidos em um e-commerce. Utilizando os conhecimentos adquiridos nas aulas, usamos uma VM com Ubuntu para realizar essa manipulação e rodar automaticamente em um horário específico.

## Primeiro passo
![evidencia_processo_de_vendas](https://github.com/user-attachments/assets/a8b4b164-f5b0-4b43-b60f-6766ce2cb961) 

Criei um executavel.sh para criar diretórios e filtrar algumas das informações contidas no .csv. Nesse código, utilizei o comando **mkdir -p** para criar um diretório, com o parâmetro "-p" para não gerar um erro caso o diretório já existisse. O comando cp foi utilizado para copiar o arquivo .csv, e a variável data foi criada para renomear o arquivo, evitando conflitos. O comando **touch** foi utilizado para criar um arquivo chamado **relatorio.txt** em uma pasta específica. Logo após, utilizei o comando **awk** para coletar colunas específicas, além de usar parênteses para encadear os comandos. O comando head foi utilizado para pegar uma quantidade específica de linhas — neste caso, 10. Em seguida, utilizei o comando echo concatenado com tail para contar o número de vendas realizadas. Após isso, movi o arquivo para a pasta backup, onde o comando zip compactou o .csv, renomeando-o com a data de execução do programa.

## Segundo passo 

![evidencia_crontab-e](https://github.com/user-attachments/assets/b674e55c-993e-48dd-9e3b-eb74dede9925)

Utilizando o Cron, foi possível agendar a execução do código para um horário específico. No meu caso, deixei o programa para rodar todos os dias, exatamente às 15:27 (3:27 pm), como demonstrado na imagem acima.

## Terceiro passo

![evidencia_consolidador](https://github.com/user-attachments/assets/a991786e-6517-460d-b2cf-ca030f4caa13)

Após o código ser executado durante quatro dias e gerar quatro relatórios, deveríamos criar um segundo executável para juntar esses quatro relatórios em um só. O código que utilizei foi bem simples, utilizando apenas o comando **cat** para copiar, **touch** para criar, e **echo** para organizar o relatório com mensagens ou espaçamento entre os relatórios.


# Dificuldades
Bem, algumas coisas me atrapalharam no processo de cumprir esse desafio, como instruções não muito claras e sujeitas a várias interpretações, coisas que só ficaram claras na última monitoria. Apesar de tudo, o Linux foi a parte mais fácil para mim, pois já tinha algum conhecimento prévio. No entanto, foi no Git e no GitHub onde mais sofri, visto que, apesar de já ter outra conta, nunca havia subido nenhum repositório. Acabei aprendendo por necessidade, já que até então só usava o site para baixar conteúdos/projetos de terceiros. 
