# Desafio 
------------------------------------------------------------------------------------------
## Resumo
------------------------------------------------------------------------------------------
Neste desafio utilizei o 'Docker' para executar arquivos python, o primeiro sendo
fornecido pelo o desafio e o segundo seria criado por mim para fazer o mesmo. 

### Primeira etapa 
------------------------------------------------------------------------------------------
#### Resumo:
Nessa etapa recebi um arquivo chamado **'carguru.py'** que me retornava um string aleatoria de uma lista e apartir dela realizar as intruções: 
##### Instruções: 
- Construir uma imagem a partir de um arquivo dockerfile que execute o arquivo que baixei (carguru.py). Após execute um container a partir da imagem criada  

##### Execução:
criação da imagem a partir do arquivo parte 1
![imagem](../Evidencias/Criação_da_imagem_parte_1.png)
criação da imagem a partir do arquivo parte 2 
![imagem](../Evidencias/Criação_da_imagem_parte_2.png) 
Aqui está a prova da criação do container 
![imagem](../Evidencias/Prova_criação_container.png) 
Execução do container pela imagem 
![imagem](../Evidencias/Prova_e_execução_imagem-container.png) 

### Segunda etapa
------------------------------------------------------------------------------------------

#### Instruções
É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta. 

##### Resposta:
------------------------------------------------------------------------------------------

Sim é possivel, pode se utilizar o comando: **"Docker restart (nome do container)/ (id do container)"**
ou se quiser executalo interativamente utiliza-se o comando:
**"Docker start -i (nome do container) / (id do container)"**  

![imagem](../Evidencias/Prova_possibilidade_de_reiniciar_um_container.png)

### Terceira etapa
Aqui eu deveria fazer exatamete oque fiz na primeira etapa porém com um codigo criado por mim. 

#### Instruções 
- Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Abaixo seguem as instruções. 

1.Criar novo script Python que implementa o algoritmo a seguir:
	- Receber uma string via input.
	- Gerar o Hash da string por meio do algoritmo SHA-1
	- Imprimir o hash em tela, utilizando o método hexdigest 
	- retornar ao passo 1

2- Criar uma imagem Docker chamada mascarar-dados que execute o script python criado anteriormente.

3-Iniciar um container a partir da imagem, enviando algumas palavras para mascararamento.

4-Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço 

------------------------------------------------------------------------------------------

*Script Python* 

![imagem](../Evidencias/Script.png)

*Script sendo executado fora do docker*

![imagem](../Evidencias/Script_funcionando.png) 

*Criação da imagem* 

![imagem](../Evidencias/Criação_mascarar-dados.png) 

*Execução pela imagem* 

![imagem](../Evidencias/Execução_pela_imagem2.png) 

*Prova da inicialização da terceira etapa pelo container*

![imagem](../Evidencias/Prova_inicialização_etapa3.png)

*Prova da existencia da imagem e do container* 

![imagem](../Evidencias/Prova_Imagem_e_Container.png)
