# Exercício 03

############### FUNÇÕES ##################

# Função para fazer linha de axteriscos
def linhaAsterisco (quantiidadeAsteriscos = 70):
    print('*' * quantiidadeAsteriscos)

# Função metragem_limpeza()
def metragem_limpeza():
    valor = 0.0

    while True:
        try: 
            metragem = int(input('Entre com a metragem da casa: '))
            if(metragem < 30 or metragem >= 700):
                print('!! Não Aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')
            else:
                break
        except ValueError:
            continue
    
    if(metragem <= 30 and metragem <300):
        valor = 60 + 0.3 * metragem
    else:
        valor = 120 + 0.5 * metragem
    return (valor)

# Função tipo_limpeza()
def tipo_limpeza():
    while True:
        valor = 0.0
        print('Entre com o tipo de limpeza: ')
        print('B - Básica - Indicada para sujeiras semanais ou quizenais')
        print('C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras')
        tipo = input()
        if(tipo == 'B'):
            valor = 1
            break
        elif(tipo == 'C'):
            valor = 1.3
            break
        else:
            print('!!!!! Opção Inválida !!!!!')

    return (valor)

# Função adicional_limpeza()
def adicional_limpeza():
    valor = 0.0
    while True:
        print('Deseja mais algum adicional?')
        print('0 - Não desejo mais nada (encerrar)')
        print('1 - Passar 10 peças de roupas - R$ 10,00')
        print('2 - Limpeza de 1 Forno/Micro-Ondas - R$ 12,00')
        print('3 - Limpeza de 1 geladeira/Freezer - R$ 20,00')
        try:
            adicional = int(input(''))
            if(adicional == 0):
                break
            elif(adicional == 1):
                valor += 10.00
                continue
            elif(adicional == 2):
                valor += 12.00
                continue
            elif(adicional == 3):
                valor += 20.00
                continue
            else:
                print('Opção Inexistente! Tente novamente.')
                continue
        except ValueError:
            print('Use o número correspondete a opção desejada!')
            continue
    return(valor)

################   INÍCIO DO PROGRAMA PRINCIPAL ##############

print('Bem-vindo ao Programa de serviços de limpeza do João Paulo Pires')
linhaAsterisco() # chamando a função para fazer a linha de asteriscos

# Menu 1 de 3
print('-' * 15, 'Menu 1 de 3 - Metragem Limpeza ', '-' * 15)
valor_metragem = metragem_limpeza()
print ('Custo referente ao tamanho da área de limpeza é: R$ {:.2f}' . format(valor_metragem))
linhaAsterisco()

# Menu 2 de 3
print('-' * 15, 'Menu 2 de 3 - Tipo Limpeza ', '-' * 15)
valor_tipo = tipo_limpeza()
if (valor_tipo == 1):
    print('Você selecionou a limpeza BÁSICA!')
else:
    print('Você selecionou a limpeza COMPLETA!')
linhaAsterisco()

#Menu 3 de 3
print('-' * 15, 'Menu 3 de 3 - Adicional Limpeza ', '-' * 15)
valor_adicional = adicional_limpeza()
print('Valor referente aos adicionais: R$ {:.2f}'. format(valor_adicional))
linhaAsterisco()

## TOTAL
valor_total = (valor_metragem * valor_tipo) + valor_adicional
print('Total: R$ {:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional {:.2f})'. format(valor_total, valor_metragem, valor_tipo, valor_adicional))
linhaAsterisco()