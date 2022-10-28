# Exercício 04

####################### FUNÇÕES #########################

# Função geradora de linha de asteriscos
def linha_asterisco(quantidade_asteriscos = 70):
    print('*' * quantidade_asteriscos)

# Função de cadastrar Funcionário, recebe o ID do funcionário como parametro
def cadastrar_funcionario(id):
    print('Código do Funcionário {}'. format(id)) # a implementar essa função
    nome_funcionario = input('Por favor, entre com o NOME: ')
    setor_funcionario = input('Por favor, entre com o SETOR: ')
    salario_funcionario = input('Por favor, entre com o SALÁRIO: ')
    funcionario = {
        'id': id,
        'nome': nome_funcionario,
        'setor': setor_funcionario,
        'salario': salario_funcionario,
    }
    return funcionario

# Função de Consulta de Funcionário
def consultar_funcionario():
    print('Consultar Funcionario') #  Função a implementar

# Função para remover funcionário
def remover_funcionario():
    print('Remover Funcionário') # Função a implementar

################## PROGRAMA PRINCIPAL ####################
print('Bem-vindo ao Controle de Funcionários do João Paulo Pires')
linha_asterisco()

# Menu Principal 
id = 700
funcionarios = []

while True:
    opcao = 0
    print ('-' * 30, ' MENU PRINCIPAL ', '-' * 30)
    print ('Escolha a opção desejada: ')
    print('1-Cadastrar Funcionário')
    print('2-Consultar Funcionário(s)')
    print('3-Remover Funcionário')
    print('4-Sair')

    ## TRATANDO OPÇÕES ##
    try:
        opcao = int(input(''))
    except ValueError:
        print('Entre com o NÚMERO de acordo com a opção desejada!')
        continue

    ## VERIFICANDO OPÇÕES ##
    # Cadastrar funcionário:
    if(opcao == 1): 
        linha_asterisco()
        print('-' * 20, ' MENU CADASTRAR FUNCIONARIO ', '-' * 20)
        funcionarios.append(cadastrar_funcionario(id).copy())
        print(funcionarios)
        id = id + 1
        continue

    # Consultar Funcionário:
    elif(opcao == 2):
        linha_asterisco()
        print('-' * 20, ' MENU CONSULTAR FUNCIONARIO(S) ', '-' * 20)
        consultar_funcionario()
        continue

    # Remover Funcionário:
    elif(opcao == 3):
        linha_asterisco()
        print('-' * 20, ' MENU REMOVER FUNCIONARIO ', '-' * 20)
        remover_funcionario()
        continue

    # Sair (encerrar o programa):
    elif(opcao == 4):
        print('Obrigado por utilizar o software!')
        break

    # Nenhuma das opções válidas:
    else:
        print('Opção inválida!! Verifique a opção desejada novamente')