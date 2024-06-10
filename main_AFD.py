from tkinter import *
import re
from numpy import append

# Ler o arquivo informado pelo usuário e gerar o AFD a partir dele
def gerarAutomato():
    try:
        arquivo = open("arquivo_AFD.txt" , 'r') # Lendo o arquivo informado pelo usuário
        automato = list()
        # Lendo cada linha do meu arquivo
        # Adicionando as informações do AFD a lista
        for linha in arquivo:
            linha = linha.replace("\n", "")
            automato.append(linha)
        arquivo.close()
        return automato
    except:
        return 'ERRO'

#Recebendo o AFD, separando seus estados e retornando-os
def separarEstados(automato):
    estados = re.split(" ", automato[1]) # Os estados estão na posição 1 da lista
    return estados

#Recebendo o AFD e separando seu alfabeto
def separarAlfabeto(automato):
    alfabeto = re.split(" ", automato[2]) # O alfabeto está na posicao 2 da lista
    alfabeto = set(alfabeto)
    return alfabeto

# Recebendo o AFD e separando seu estado inicial
def separarEstadoInicial(automato):
    estadoInicial = automato[3] ## O estado inicial está na posicao 3 da lista
    return estadoInicial

# Recebendo o AFD e separando seus estados finais
def separarEstadosFinais(automato):
    estadoFinal = re.split(" ", automato[4]) # Os estados finais estão a posicao 4 da lista
    return estadoFinal

# Recebendo o automato e separando suas transições
def lerRegrasDeTransicao(automato):
	transicoes = {} #Criando o dicionário 
	# Percorrendo as informações do AFD a partir da linha 5
	for i in range(5, len(automato)):
		items = automato[i].split(" ") # Lendo a linha do arquivo e adicionando a lista
		index = items[0] + " " + items[2] # Definindo a chave para o dicionário
		transicoes[index] = items[1] # Adicionando as informações ao dicionário
	return transicoes

# Verificando se a palavra informada pelo usuário é reconhecida ou não pelo AFD
def verificarPalavra(alfabeto, estadoInicial, estadosFinais, transicoes, palavra):
    validacao = False # Usada para o retorno do resultado da verificação
    estadoAtual = estadoInicial
    # Percorrendo cada letra da minha palavra
    for letra in palavra:
        # Verificando se a letra está contida no alfabeto
        # Caso esteja, irá atualizar o estado atual do AFD
        # Caso não esteja, irá retornar -1 signifcando que houve um erro
        if letra in alfabeto:
            estadoAtual = transicoes[estadoAtual + " " + letra]
        else:
            return -1
    # Verificando se o estadoAtual existe na lista de estados finais
    # Caso exista, o AFD reconhece a palavra 
    if estadoAtual in estadosFinais:
        validacao = True

    return validacao

def mostrarResultado(validacao, palavra):
    # Se o AFD reconheceu a palavra
    if validacao == True:
        mensagem = "O AFD reconhece a palavra " + palavra
    # Se o AFD não reconheceu a palavra
    elif validacao == False:
        mensagem = "O AFD não reconhece a palavra " + palavra    
    # Existem simbolos que não estão no alfabeto do autômato
    else:
        mensagem = "A palavra " + palavra + " possui um simbolo que não está no alfabeto"
    
    # Atribuindo ao label a mensagem a ser exibida
    txt_info["text"] = str(mensagem)

def principal():
    automato = gerarAutomato()
    if automato != 'ERRO':
        alfabeto = separarAlfabeto(automato)
        print(alfabeto)
        estadoInicial = separarEstadoInicial(automato)
        print(estadoInicial)
        estadosFinais = separarEstadosFinais(automato)
        print(estadosFinais)
        transicoes = lerRegrasDeTransicao(automato)
        print(transicoes)
        palavra = input_Palavra.get()
        print(palavra)
        validacao =  verificarPalavra(alfabeto, estadoInicial, estadosFinais, transicoes, palavra)
        print(validacao)
        mostrarResultado(validacao, palavra)
    else:
        txt_info["text"] = "Informe um arquivo válido!"

janela = Tk() # Criando a janela principal

janela.title("Máquina de Autômatos") # Definindo o titulo da janela

# Criando o label de texto da palavra e atribuindo a ele uma posição na janela
txt_inputPalavra = Label(janela, text="Informe a palavra: ")
txt_inputPalavra.grid(column=0, row=1, padx=10, pady=10 )

# Criando um entry pra receber a palavra e atribuindo a ele uma posição na janela
input_Palavra = Entry(janela)
input_Palavra.grid(column=1, row=1, padx=10, pady=10)

# Criando um botão para mostrar o resultado e atribuindo a ele uma posicao na janela
btn_MostraInfo = Button(janela, text="Buscar", command=principal)
btn_MostraInfo.grid(column=0, row=3, padx=10, pady=10)

# Criando um label de texto para mostrar as informações e atribuindo a ele uma posicao na janela
txt_info = Label(janela, text="")
txt_info.grid(column=0, row=4, padx=10, pady=10)

janela.mainloop()