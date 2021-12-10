AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('Agenda vazia.')


def buscar_contato(contato):
    try:
        print("Nome: ", contato)
        print('Telefone: ', AGENDA[contato]['tel'])
        print('Email: ', AGENDA[contato]['email'])
        print('Endereço: ', AGENDA[contato]['endereco'])
        print('------------------------------------------')
    except KeyError:
        print('Contato inexistente.')
    except Exception as error:
        print('Um erro inesperado ocorreu.')
        print(error)


def ler_detalhes_contato():
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input('Endereço: ')

    return telefone, email, endereco


def inserir_editar_contato(contato, tel, email, endereco):
    nome = contato.lower()
    AGENDA[nome] = {
        'tel': tel,
        'email': email,
        'endereco': endereco
    }
    salvar_agenda()
    print('Contato ({}) adicionado/editado com sucesso.'.format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar_agenda()
        print()
        print('Contato ({}) excluído com sucesso.'.format(contato))
        print()
    except KeyError:
        print('Contato inexistente.')
    except Exception as error:
        print('Um erro inesperado ocorreu.')
        print(error)


def exportar_contatos(file_name):
    try:
        with open(file_name, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato, telefone, email, endereco))

        if file_name != 'database.csv':
            print()
            print('Agenda exportada com sucesso.')
            print()
    except Exception as e:
        print('Algum erro ocorreu.')
        print(e)


def importar_contatos(file_name):
    try:
        with open(file_name, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                if detalhes:
                    nome = detalhes[0]
                    telefone = detalhes[1]
                    email = detalhes[2]
                    endereco = detalhes[3]

                    inserir_editar_contato(nome, telefone, email, endereco)
                else:
                    print('Agenda vazia')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as error:
        print('Erro inesperado ocorreu :', error)


def salvar_agenda():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                if detalhes:
                    nome = detalhes[0]
                    telefone = detalhes[1]
                    email = detalhes[2]
                    endereco = detalhes[3]

                    AGENDA[nome] = {
                        'tel': telefone,
                        'email': email,
                        'endereco': endereco
                    }
                else:
                    print('Agenda vazia')
        print('Database carregado com sucesso.')
        print(len(linhas), ' contato(s) importado(s)')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as error:
        print('Erro inesperado ocorreu :', error)


def imprimir_menu():
    print('------------------------------------------')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar agenda')
    print('7 - Importar agenda')
    print('0 - Fechar agenda')
    print('------------------------------------------')

carregar()
while True:
    imprimir_menu()
    opcao = input("Escolha um opção: ")
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input("Digite o nome do contato: ")
        buscar_contato(contato.lower())
    elif opcao == '3':
        contato = input("Nome do contato: ")

        try:
            AGENDA[contato]
            print('Contato já existente.')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            inserir_editar_contato(contato.lower(), telefone, email, endereco)

    elif opcao == '4':
        contato = input("Nome do contato: ")

        try:
            AGENDA[contato]
            print('Editando contato: ', contato)
            telefone, email, endereco = ler_detalhes_contato()
            inserir_editar_contato(contato.lower(), telefone, email, endereco)
        except KeyError:
            print('Contato inexistente.')

    elif opcao == '5':
        contato = input('Nome do contato: ')
        excluir_contato(contato.lower())
    elif opcao == '6':
        file_name = input('Digite o nome do arquivo a ser salvo: ')
        exportar_contatos(file_name)
    elif opcao == '7':
        file_name = input('Insira o caminho até o arquivo: ')
        importar_contatos(file_name)
    elif opcao == '0':
        print('Agenda fechada.')
        break
    else:
        print('Opção inválida.')