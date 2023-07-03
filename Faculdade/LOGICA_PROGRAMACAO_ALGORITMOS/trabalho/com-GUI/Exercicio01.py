#Exercício 01
from tkinter import*

def calculdora_preco():
    quantidadeProduto = int(quantidade.get())
    valorProduto = float(preco.get())
    frete = 0.0 #declarando variável frete e inicializnado com 0
    if (quantidadeProduto < 11): 
        frete = 30 # se quantidade estiver entre 0 e 10 frete recebe 30
    elif (quantidadeProduto >= 11 and quantidadeProduto < 101):
        frete = 60 # se quantidade estiver entre 11 e 100 frete recebe 60
    elif (quantidadeProduto >= 101 and quantidadeProduto < 1001):
        frete = 120 # se quantidade estiver entre 101 e 1000 frete recebe 120
    else:
        frete = 240 # se quantidade for maior que 1000 frete recebe 240

    texto_saida1['text'] = ('Valor sem frete foi: R$ {:.2f} '. format(valorProduto * quantidadeProduto)) # mostra valor sem o frete
    texto_saida2['text'] = ('Valor com frete foi: R$ {:.2f} '. format(valorProduto * quantidadeProduto + frete)) # mostra valor com o frete


##################################### GUI COM TKINTER #####################################

janela = Tk()
janela.geometry("270x150")
janela.title("Cálcular Preço e Frete!")
#texto_saudacao = Label(janela, text="Seja bem vindo a loja do João Paulo Pires")
#texto_saudacao.grid(column=0, row=0)

# Textos para as caixas de entrada
texto_entrada1 = Label(janela, text= "Valor do produto: ")
texto_entrada1.grid(column=0, row=1)
texto_entrada2 = Label(janela, text= "Quantidade do produto: ")
texto_entrada2.grid(column=0, row=2)

# Caixa de Entradas
preco = Entry(janela, width=10)
preco.grid(column=1, row = 1)
quantidade = Entry(janela, width=10)
quantidade.grid(column= 1, row= 2)

# Botão de calcular
botao = Button(janela, text="Calcular", command=calculdora_preco)
botao.grid(column=0, row = 4)

# Saidas 
texto_saida1 = Label(janela, text="")
texto_saida1.grid(column=0, row=5, padx=10, pady=5)
texto_saida2 = Label(janela, text="")
texto_saida2.grid(column=0, row=6, padx=10, pady=5)

janela.mainloop()