#Exercício 01

print ('Seja bem vindo a loja do João Paulo Pires')
valorProduto = float (input ('Entre com o valor do produto: ')) # lendo valor do produto
quantidadeProduto = float (input ('Entre com a quantidade de produto: ')) # Lendo a quantidade de produto

frete = 0.0 #declarando variável frete e inicializnado com 0

if (quantidadeProduto < 11): 
    frete = 30 # se quantidade estiver entre 0 e 10 frete recebe 30
elif (quantidadeProduto >= 11 and quantidadeProduto < 101):
    frete = 60 # se quantidade estiver entre 11 e 100 frete recebe 60
elif (quantidadeProduto >= 101 and quantidadeProduto < 1001):
    frete = 120 # se quantidade estiver entre 101 e 1000 frete recebe 120
else:
    frete = 240 # se quantidade for maior que 1000 frete recebe 240

print ('valor sem frete foi: R$ {:.2f} '. format(valorProduto * quantidadeProduto)) # mostra valor sem o frete
print ('Valor com frete foi: R$ {:.2f} '. format(valorProduto * quantidadeProduto + frete)) # mostra valor com o frete