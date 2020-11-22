from os import system
from sys import exit
from random import randint
system('clear')

# Essa função serve para criar o logo da empresa
def logo_icaro():
    print('_' * 76)
    print(' ' * 9, '/')
    print(' ' * 8, '/')
    print(' ' * 5, '=' * 7, ' ' * 5, '=' * 7, ' ' * 5, '=' * 7, ' ' * 5, '=' * 7, ' ' * 5, '=' * 8)
    print(' ' * 8, '|', ' ' * 8, '|', ' ' * 10, '|', ' ' * 5, '|', ' ' * 4, '|', ' ' * 4, '|', ' ' * 4, '|', ' ' * 4,
          '|')
    print(' ' * 8, '|', ' ' * 8, '|', ' ' * 10, '|', ' ' * 5, '|', ' ' * 4, '|', ' ' * 4, '|', ' ' * 4, '|', ' ' * 4,
          '|')
    print(' ' * 8, '|', ' ' * 8, '|', ' ' * 10, '|', ' ' * 5, '|', ' ' * 4, '|', ' ' * 4, '|', ' ' * 4, '|', ' ' * 4,
          '|')
    print(' ' * 8, '|', ' ' * 8, '|', ' ' * 10, '=' * 9, ' ' * 4, '=' * 7, ' ' * 5, '|', ' ' * 4, '|')
    print(' ' * 8, '|', ' ' * 8, '|', ' ' * 10, '|', ' ' * 5, '|', ' ' * 4, '|', '\\', ' ' * 9, '|', ' ' * 4, '|')
    print(' ' * 8, '|', ' ' * 8, '|', ' ' * 10, '|', ' ' * 5, '|', ' ' * 4, '|', ' ', '\\', ' ' * 7, '|', ' ' * 4, '|')
    print(' ' * 5, '=' * 7, ' ' * 5, '=' * 7, ' ' * 4, '|', ' ' * 5, '|', ' ' * 4, '|', '   ', '\\', ' ' * 5, '=' * 8)
    print('_' * 76)

logo_icaro()

# Lista com os DDDs do estado de São Paulo
lista_DDDs = ['11', '12', '13', '14', '15', '16', '17', '18', '19']

# Lista com os respectivas regiões dos DDDs da lista anterior
lista_cidades_DDDs = ['São Paulo/Jundiaí/Itu/Bragança Paulista', 'São José dos Campos/Taubaté/Vale do Paraíba',
                      'Santos/São Vicente/Baixada Santista/Vale do Ribeira', 'Bauru/Marília/Jaú/Botucatu',
                      'Sorocaba/Itapetininga/Itapeva', 'Ribeirão Preto/Franca/São Carlos/Araraquara',
                      'São José do Rio Preto/Catanduva/Barretos/Votuporanga', 'Presidente Prudente/Araçatuba/Birigui/'
                      'Assis', 'Campinas/Piracicaba/Limeira/Americana']

# Dicionário de com as informações dos usuários
dicio_usuarios_login = {}

# Lista com as informações dos usuários separadas por índices
lista_usuarios_login = []

# Aqui o usuário escolhe se quer se logar ou se cadastrar
print('Digite [1] para fazer login ou [2] para criar uma conta:')
opcao_entrada = str(input('Opção: '))

# Limpa o terminal
system('clear')

# Área de login ou cadastro
while True:
    # Essa é a parte do login
    if opcao_entrada in '1[1]':
        print('-=' * 15, 'LOGIN', '=-' * 15)
        login_login_primario = str(input('Email: '))
        senha_login_primario = str(input('Senha: '))
        system('clear')
        print('Você ainda não é cadastrado. Se cadastre precionando [2]')
        exit()

    # Aqui é a do cadastro
    elif opcao_entrada in '2[2]':
        print('-=' * 17, 'CADASTRO', '=-' * 16)
        print('Preencha os campos a seguir com as informações requisitadas!')
        login_cadastro = str(input('Informe o seu email: '))
        senha_cadastro = str(input('Crie uma senha com oito dígitos: '))

        # Verificador de senha com oito dígitos
        contador_senha_cadastro = 0
        while True:
            for contador_senha_cadastro in range(len(senha_cadastro)):
                contador_senha_cadastro += 1
            if contador_senha_cadastro != 8:
                print('O número de caracteres digitados é inválido!')
                senha_cadastro = str(input('Digite a senha novamente: '))
            else:
                break

        senha_cadastro_confirmacao = str(input('Confirme a sua senha: '))

        # Essa parte serve para caso o usuário digite senhas diferentes nos campos
        while True:
            for contador_senha_cadastro in range(len(senha_cadastro_confirmacao)):
                contador_senha_cadastro += 1
            if contador_senha_cadastro != 8:
                print('O número de caracteres digitados é inválido!')
                senha_cadastro_confirmacao = str(input('Confirme a senha novamente: '))
            elif senha_cadastro != senha_cadastro_confirmacao:
                print('Ambas as senhas não coincidem!')
                senha_cadastro_confirmacao = str(input('Confirme a senha novamente: '))
            else:
                break

        celular_cadastro = str(input('Digite o seu número de celuar: ')).replace(" ", "")

        # Caso o usuário digite um número de celular fora dos padrões esperados
        while True:
            if len(celular_cadastro) != 11 or celular_cadastro.isalpha() is True:
                print('Número inválido!')
                celular_cadastro = str(input('Digite o seu número de celuar: ')).replace(" ", "")
            else:
                break

        # Descobrindo a região que o usuário provavelmente mora, baseado no DDD
        DDD = celular_cadastro[0] + celular_cadastro[1]
        if DDD in lista_DDDs:
            contador_DDD = 0
            for i in lista_DDDs:
                if i == DDD:
                    regiao = lista_cidades_DDDs[contador_DDD]
                contador_DDD += 1

        # Limpa o terminal
        system('clear')

        # Pergunta caso o usuário queira cadastrar o cartão de crédito agora ou não
        print('-=' * 14, 'CADASTRO CARTÃO', '=-' * 16)
        cadastrar_cartao_cadastro = str(input('Deseja cadastrar o seu cartão para facilitar futuras compras? [S/N] '))
        from time import sleep
        while True:
            if cadastrar_cartao_cadastro not in 'sSnN':
                print('Opção inválida!')
                cadastrar_cartao_cadastro = str(
                    input('Deseja cadastrar o seu cartão para facilitar futuras compras? [S/N] '))
            else:
                break
        if cadastrar_cartao_cadastro in 'Ss':

            # Limpa o terminal
            system('clear')

            # Esse código serve para cadastrar um cartão de crédito
            print('-=' * 14, 'CADASTRO CARTÃO', '=-' * 16)
            numero_cartao = str(input('Digite o número do cartão: ')).replace(" ", "")

            # Aqui se verifica se o cartão tem dezesseis dígitos como o esperado
            contador_numero_cartao = 0
            while True:
                for contador_numero_cartao in range(len(numero_cartao)):
                    contador_numero_cartao += 1
                if contador_numero_cartao != 16:
                    print('Quantidade de caracteres invalida!')
                    numero_cartao = str(input('Digite o número do cartão novamente: ')).replace(" ", "")
                else:
                    break

            titular_cartao = str(input('Digite o nome do titular: ')).upper()
            validade_cartao = str(input('Digite a data de validade do cartão (mm/aa): ')).replace("//", " ")

            # Verificado se o usuário digitou apenhas números e se foi no padrão solicitado
            while True:
                if validade_cartao.isalnum() is True:
                    print('Validade do cartão inválida!')
                    validade_cartao = str(input('Digite a data de validade do cartão novamente (mm/aa): ')).replace(
                        "//", " ")
                else:
                    break

            codigo_seguranca_cartao = str(input('Digite o código de segurança do cartão: '))

            # Verificando se o usuário digitou corretamento o código de segurança do cartão
            contador_codigo_seguranca_cartao = 0
            while True:
                for contador_codigo_seguranca_cartao in range(len(codigo_seguranca_cartao)):
                    contador_codigo_seguranca_cartao += 1
                if contador_codigo_seguranca_cartao != 3:
                    print('Código de segurança inválido!')
                    codigo_seguranca_cartao = str(input('Digite novamente o código de segurança: '))
                elif codigo_seguranca_cartao.isalpha() is True:
                    print('Código de segurança inválido!')
                    codigo_seguranca_cartao = str(input('Digite novamente o código de segurança: '))
                else:
                    break

        # Limpa o terminal
        system('clear')

        print('Redirecionando para a tela inicial...')
        sleep(2)

        # Limpa o terminal
        system('clear')
        break

    # Caso o usuário digite uma opção que não seja logar ou cadastrar
    else:
        print('Opção inválida! Tente novamente:')
        opcao_entrada = input(str('Opção: '))

# PROVISÓRIO Fecha o programa quando o usuário loga pela primeira vez
if opcao_entrada in 'loginLoginLOGIN':
    exit()

# Aqui o usuário escolhe se quer se logar ou se cadastrar pela segunda vez
lista_viagens = []
print('Digite "logar" para entrar ou "cadastrar" para criar uma conta:')
opcao_entrada = str(input('Opção: '))

while True:
    if opcao_entrada in 'cadastroCadastroCADASTRO':
        system('clear')
        print('-=' * 14, 'CADASTRO', '=-' * 14)
        print('Você já se cadastrou! Digite "login" para logar na plataforma.')
        opcao_entrada = str(input('Opção: '))
    elif opcao_entrada in 'loginLoginLOGIN':
        system('clear')
        print('-=' * 15, 'LOGIN', '=-' * 15)
        login_login_secundario = str(input('Email: '))
        senha_login_secundario = str(input('Senha: '))
        system('clear')
        print('BEM VINDO AO ÍCARO TRAVELS!!!')
        print('-=' * 33)
        print('Escolha os pacotes de viagens que desejar:')
        #Aqui ele escolhe o que ele vai comprar
        while True:
            pacotes_viagens = int(input(('Praia pra que ti quero [1]\n'
                  'Pacotes Orlando! [2]\n'
                  'Baladas pelo mundo! [3]\n'
                  'Pacote sertão nordestino [4]\n'
                  'Eurotrip [5]\n'
                    'Opção: ')))
            system('clear')
            if pacotes_viagens != 1 or 2 or 3 or 4 or 5:
                print('Opção inválida')
                print('-=' * 33)
            if pacotes_viagens == 1:
                print('Caraguatatuba [1]\n Preço: R$1500\nBertioga [2]\n Preço: R$1500\nPraia do Rosa [3]\n Preço: '
                      'R$1500\n')
                pacotes_viagens_praia = int(input('Opção: '))
                lista_viagens.append(pacotes_viagens_praia)
                break
            elif pacotes_viagens == 2:
                print('Magic Kingdom [1]\n Preço: R$1500\nUniversal [2]\n Preço: R$1500\nEpicote [3]\n Preço: '
                      'R$1500\n')
                pacotes_viagens_orlando = int(input('Opção: '))
                lista_viagens.append(pacotes_viagens_orlando)
                break
            elif pacotes_viagens == 3:
                print('Ibiza [1]\n Preço: R$1500\nBaile da Gaiola [2]\n Preço: R$1500\nBaladex [3]\n Preço: '
                      'R$1500\n')
                pacotes_viagens_balada = int(input('Opção: '))
                lista_viagens.append(pacotes_viagens_balada)
                break
            elif pacotes_viagens == 4:
                print('Caatinga [1]\n Preço: R$1500\nPiauí [2]\n Preço: R$1500\nFortaleza [3]\n Preço: '
                      'R$1500\n')
                pacotes_viagens_nordeste = int(input('Opção: '))
                lista_viagens.append(pacotes_viagens_nordeste)
                break
            elif pacotes_viagens == 5:
                print('Reino Unido [1]\n Preço: R$1500\nFrança [2]\n Preço: R$1500\nPortugual [3]\n Preço: '
                      'R$1500\n')
                pacotes_viagens_eurotrip = int(input('Opção: '))
                lista_viagens.append(pacotes_viagens_eurotrip)
                break
        print('Compra efetuada com sucesso')
        break
    else:
        print('Opção inválida! Tente novamente')
        opcao_entrada = str(input('Opção: '))
        break
system('clear')
# Aqui é como ele pretende pagar
print('Como deseja pagar?')
forma_pagamento = int(input(' Boleto [1]\n Cartão de Crédito [2]\n Cartão Ícaro [3]\n Opção: '))
if forma_pagamento == 1:
    # Esse código serve para gerar um boleto
    print('Gerando boleto...')
    sleep(3)
    print('Boleto gerado!\n')
    for boleto1 in range(0, 10):
        print(f'{randint(0, 9)}', end='')
        if boleto1 == 4:
            print('.', end='')
    print(' ', end='')
    for boleto2 in range(0, 11):
        print(f'{randint(0, 9)}', end='')
        if boleto2 == 4:
            print('.', end='')
    print(' ', end='')
    for boleto3 in range(0, 11):
        print(f'{randint(0, 9)}', end='')
        if boleto3 == 4:
            print('.', end='')
    print(f' {randint(0, 9)} ', end='')
    for boleto4 in range(0, 14):
        print(f'{randint(0, 9)}', end='')
    print()
    imprimir_boleto = int(input('Digite 1 para imprimir o boleto: '))
    if imprimir_boleto == 1:
        #system('clear')
        print('Tá loco! Isso daqui não imprime nada não.')
        sleep(1)
elif forma_pagamento == 2:
    print('Processando os dados...')
    sleep(3)
    print('Transação feita com sucesso!')
elif forma_pagamento == 3:
    print('Compra feita com sucesso!')
system('clear')
print('Obrigado por comprar com a Ícaros! Boa viagem e volte sempre!!!')
print()
import gzip
print(gzip.decompress(b'\x1f\x8b\x08\x00\x95\x10\xe0R\x02\xffSPP\xf0\xc9/KU\x80\x03\x10\x8f\x0bB\xa1c.l\x82dJ\xe0\xb0\x01\xe6\x02\x0cATa.T\xf7\x02\x00\xd9\x91g\x05\xc5\x00\x00\x00').decode('ascii'))
