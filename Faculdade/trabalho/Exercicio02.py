# Exercício 02

from contextlib import nullcontext


print('Bem-vindo(a) a Sorveteria do João Paulo Pries')
print('-------------------------------------------- Cardápio -------------------------------------------')
print('| Código | Descrição              | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('| TR     | Sabores Tradicionais   | R$ 6,00           | R$ 10,00           |  R$ 18,00          |')
print('| ES     | Sabores Especiais      | R$ 7,00           | R$ 12,00           |  R$ 21,00          |')
print('| PR     | Sabores Premium        | R$ 8,00           | R$ 14,00           |  R$ 24,00          |')
print('-------------------------------------------------------------------------------------------------')

x = 'S'
precoSorvete = 0.0
soma = 0.0
while (x == 'S'):
    tamanhoSorvete = input('Entre com o TAMANHO do Pote desejado (P/M/G): ')
    codigoSorvete = input ('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')

    #Validando Tamanho 
    if (tamanhoSorvete !='P' and tamanhoSorvete != 'M' and tamanhoSorvete != 'G'):
        print ('!!!!!!! TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!!!')  
        continue

    #Validando Código
    elif (codigoSorvete != 'TR' and codigoSorvete != 'ES' and codigoSorvete != 'PR'):
        print ('!!!!!!! TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!!!')  
        continue
    else:
        #linha 1 (TR)
        if (codigoSorvete == 'TR' and tamanhoSorvete == 'P'):
            precoSorvete = 6
            soma+= precoSorvete
        elif (codigoSorvete == 'TR' and tamanhoSorvete == 'M'):
            precoSorvete = 10
            soma+= precoSorvete
        elif (codigoSorvete == 'TR' and tamanhoSorvete == 'G'):
            precoSorvete = 18
            soma+= precoSorvete

        #linha 2 (ES)
        elif (codigoSorvete == 'ES' and tamanhoSorvete == 'P'):
            precoSorvete = 7
            soma+= precoSorvete
        elif (codigoSorvete == 'ES' and tamanhoSorvete == 'M'):
            precoSorvete = 12
            soma+= precoSorvete
        elif (codigoSorvete == 'ES' and tamanhoSorvete == 'G'):
            precoSorvete = 21
            soma+= precoSorvete

        #linha 3 (PR)
        elif (codigoSorvete == 'PR' and tamanhoSorvete == 'P'):
            precoSorvete = 8
            soma+= precoSorvete
        elif (codigoSorvete == 'PR' and tamanhoSorvete == 'M'):
            precoSorvete = 14
            soma+= precoSorvete
        elif (codigoSorvete == 'PR' and tamanhoSorvete == 'G'):
            precoSorvete = 24
            soma+= precoSorvete
        
    # Confirmação de pedido do Usuário
    print('Você pediu um sorvete {} de R$ {:.2f}'. format(tamanhoSorvete, precoSorvete))
    precoSorvete = 0
    print('----------------------------------------------------------')

    x = input ('Deseja pedir mais alguma coisa (S/N): ')
    if(x == 'N'):
        break

print('O total a ser pago é: R$ {:.2f}'. format(soma))