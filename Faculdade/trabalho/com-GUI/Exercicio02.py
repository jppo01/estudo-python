# Exercício 02
from tkinter import*
from tkinter import ttk
import sys

#criando arquivo para salvar lista de pedido
arquivo = open('lista_pedido.txt','w')
arquivo.close()

#criando arquivo de texto para armazenar as somas do pedido
arquivo = open('soma.txt', 'w')
arquivo.write('0')
arquivo.close()

def reset():
    #criando arquivo para salvar lista de pedido
    arquivo = open('lista_pedido.txt','w')
    arquivo.close()
    arquivo = open('soma.txt', 'w')
    arquivo.write('0')
    arquivo.close()
    arquivo = open ('soma.txt')
    soma = float(arquivo.read())
    arquivo.close()

    txt_adicionado["text"] = "Novo pedido vazio"
    txt_subtotal["text"] = ("Subtotal: R$ {:.2f}". format(soma))

    #criando arquivo de texto para armazenar as somas do pedido
    arquivo = open('soma.txt', 'w')
    arquivo.write('0')
    arquivo.close()

def finalizar():
    arquivo = open('soma.txt')
    soma = float(arquivo.read())
    txt_adicionado["text"] = ("Pedido finalizado!")
    txt_subtotal["text"] = ("Total a pagar: R$ {}". format(soma))

def adicionar():
    codigoSorvete = box_sabor.get()
    tamanhoSorvete = box_tamanho.get()
    subsoma = 0.0
    #linha 1 (TR)
    if (codigoSorvete == 'Tradicional' and tamanhoSorvete == 'P'):
        precoSorvete = 6
        subsoma = subsoma + precoSorvete
    elif (codigoSorvete == 'Tradicional' and tamanhoSorvete == 'M'):
        precoSorvete = 10
        subsoma = subsoma + precoSorvete
    elif (codigoSorvete == 'Tradicional' and tamanhoSorvete == 'G'):
        precoSorvete = 18
        subsoma = subsoma + precoSorvete

    #linha 2 (ES)
    elif (codigoSorvete == 'Especial' and tamanhoSorvete == 'P'):
        precoSorvete = 7
        subsoma = subsoma + precoSorvete
    elif (codigoSorvete == 'Especial' and tamanhoSorvete == 'M'):
        precoSorvete = 12
        subsoma = subsoma + precoSorvete
    elif (codigoSorvete == 'Especial' and tamanhoSorvete == 'G'):
        precoSorvete = 21
        subsoma = subsoma + precoSorvete

    #linha 3 (PR)
    elif (codigoSorvete == 'Premium' and tamanhoSorvete == 'P'):
        precoSorvete = 8
        subsoma = subsoma + precoSorvete
    elif (codigoSorvete == 'Premium' and tamanhoSorvete == 'M'):
        precoSorvete = 14
        subsoma = subsoma + precoSorvete
    elif (codigoSorvete == 'Premium' and tamanhoSorvete == 'G'):
        precoSorvete = 24
        subsoma = subsoma + precoSorvete

    arquivo = open('soma.txt')
    soma = float(arquivo.read())
    arquivo.close()
    soma += subsoma

    arquivo = open('soma.txt', 'w')
    arquivo.write(str(soma))
    arquivo.close()

    arquivo = open('lista_pedido.txt', 'a')
    arquivo.write("Sabor: {} Tamanho: {} Valor: R$ {:.2f}\n". format(codigoSorvete, tamanhoSorvete, precoSorvete))
    arquivo.close()
    arquivo = open('lista_pedido.txt')
    lista = str(arquivo.read())
    arquivo.close()

    txt_adicionado["text"] = lista
    txt_subtotal["text"] = ("Subtotal: R$ {:.2f}". format(soma))

################################### GUI com TKINTER ###########################################

janela = Tk()
janela.geometry("700x400")
janela.title("Loja Sorvete")

txt_sabor = Label(janela, text="Escolha o sabor")
txt_sabor.grid(column=0, row=0, padx=100)
sabor = ["Tradicional","Especial", "Premium"]
box_sabor = ttk.Combobox(janela, value=sabor)
box_sabor.grid(column=0, row=1, padx=100)
box_sabor.set("Tradicional")

txt_tamanho = Label(janela, text="Escolha o Tamanho")
txt_tamanho.grid(column=1, row=0)
tamanho = ["P", "M", "G"]
box_tamanho = ttk.Combobox(janela, value=tamanho)
box_tamanho.grid(column=1, row=1)
box_tamanho.set("M")

btn_adicionar = Button(janela, text="Adicionar", command=adicionar)
btn_adicionar.grid(column=2, row=1)
btn_adicionar = Button(janela, text="Finalizar", command=finalizar)
btn_adicionar.grid(column=2, row=2)
btn_reset = Button(janela, text="Novo Pedido", command=reset)
btn_reset.grid(column=2, row=3)

txt_adicionado = Label(janela, text="")
txt_adicionado.grid(column=0, row=3, padx=50)
txt_subtotal = Label(janela, text="")
txt_subtotal.grid(column=0, row=4, padx= 50)

janela.mainloop()