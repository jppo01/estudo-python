# Exercício 04

####################### FUNÇÕES #########################

# Função geradora de linha de asteriscos
def linha_asterisco(quantidade_asteriscos = 70):
    print('*' * quantidade_asteriscos)

# Função de cadastrar Funcionário, recebe o ID do funcionário como parametro
def cadastrar_funcionario(id):
    print('Código do Funcionário {}'. format(id))
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
    while True:
        print("Escolha a opção desejada:\n",
            "1-Consultar Todas as Funcionários\n",
            "2-Consultar Funcionário por Id\n",
            "3-Consultar Funcionário(s) por Setor\n",
            "4-Retornar")
        # Tratando exceção
        try:
            opcao = int(input('>>'))
            # Testando as opções
            if (opcao == 1): # consultar todos os funcionários
                print('opcao 1')
                for funcionario in funcionarios:
                    for key, value in funcionario.items():
                        print ( '{}: {}'. format(key, value))
                    print('-' * 30) # separar com linha de um funcionáiro para outro

            elif (opcao == 2): # Consultar Funcionário por Id
                try:     
                    id_informado = int(input('Informe o ID a ser consultado: '))
                    for funcionario in funcionarios:
                        if(funcionario['id'] == id_informado):
                            for key, value in funcionario.items():
                                print ( '{}: {}'. format(key, value)) 
                            print('-' * 30)
                except:
                    print ('O ID de cada funcionário é um número')

            elif (opcao == 3): # Consultar funcionário por setor
                setor_informado = input('Informe o setor desejado: ')
                for funcionario in funcionarios:
                    if(funcionario['setor'] == setor_informado):
                        for key, value in funcionario.items():
                            print('{}: {}'. format(key, value))
                        print ('' * 30)

            elif (opcao == 4 ): # Sair do Menu Consultar
                break
            else:
                print ('!!! Opção inválida !!! Escolha um número válido!')

        except ValueError:
            print ('Digite o NÚMERO correspondente a opção desejada!')
            continue

        


# Função para remover funcionário
def remover_funcionario():
    while True:
        try:
            id_informado = int(input('Entre com o ID do funcionário a ser removido: '))
            for funcionario in funcionarios:
                if(funcionario['id'] == id_informado):
                    funcionarios.remove(funcionario)
                    print('Funcionario {} removido com sucesso!'. format(funcionario['id']))
            break
        except:
            print("!!! Falha !!!",
                  "Informe o ID (valor numerico) do funcionário a ser removido!"
                  )
            continue
################## PROGRAMA PRINCIPAL ####################
print('Bem-vindo ao Controle de Funcionários do João Paulo Pires')
linha_asterisco()

# Menu Principal 
id = 700
funcionarios = []

while True:
    opcao = 0
    print ('-' * 30, ' MENU PRINCIPAL ', '-' * 30)
    print ("Escolha a opção desejada:\n",
           "1-Cadastrar Funcionário\n",
           "2-Consultar Funcionário(s)\n",
           "3-Remover Funcionário\n",
           "4-Sair")

    ## TRATANDO EXCEÇÕES ##
    try:
        opcao = int(input('>> '))
    except ValueError:
        print('Entre com o NÚMERO de acordo com a opção desejada!')
        continue

    ## VERIFICANDO OPÇÕES ##
    # Cadastrar funcionário:
    if(opcao == 1): 
        linha_asterisco()
        print('-' * 20, ' MENU CADASTRAR FUNCIONARIO ', '-' * 20)
        funcionarios.append(cadastrar_funcionario(id).copy())
        print('Funcionário {} cadastrado!'. format(id))
        id += 1
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