import os
# Lista com os DDDs do estado de São Paulo
lista_DDDs = ['11', '12', '13', '14', '15', '16', '17', '18', '19']

# Lista com os respectivas regiões dos DDDs da lista anterior
lista_cidades_DDDs = ['São Paulo/Jundiaí/Itu/Bragança Paulista', 'São José dos Campos/Taubaté/Vale do Paraíba',
                      'Santos/São Vicente/Baixada Santista/Vale do Ribeira', 'Bauru/Marília/Jaú/Botucatu',
                      'Sorocaba/Itapetininga/Itapeva', 'Ribeirão Preto/Franca/São Carlos/Araraquara',
                      'São José do Rio Preto/Catanduva/Barretos/Votuporanga', 'Presidente Prudente/Araçatuba/Birigui/'
                      'Assis', 'Campinas/Piracicaba/Limeira/Americana']

# Aqui o usuário escolhe se quer se logar ou se cadastrar
print('Digite "login" para entrar ou "cadastrar" para criar uma conta:')
opcao_entrada = str(input('Opção: '))

# Limpa o terminal
os.system('clear')

# Área de login ou cadastro
while True:
    # Essa é a parte do login
    if opcao_entrada in 'LoginloginLOGIN':
        print('-=' * 10, 'LOGIN', '=-' * 10)
        login_login_primario = str(input('Email: '))
        senha_login_primario = str(input('Senha: '))
        break

    # Aqui é a do cadastro
    elif opcao_entrada in 'CadastrocadastroCADASTRO':
        print('-=' * 9, 'CADASTRO', '=-' * 9)
        print('Preencha os campos a seguir com as informações requisitadas!')
        login_cadastro = str(input('Informe o seu email: '))
        senha_cadastro = str(input('Crie uma senha com oito dígitos: '))

        # Verificador de senha com oito dígitos
        contador_senha_cadastro = 0
        while True:
            for contador_senha_cadastro in range(len(senha_cadastro)):
                contador_senha_cadastro += 1
            if contador_senha_cadastro != 8:
                print('Número de caracteres inválido! Tente novamente')
                senha_cadastro = str(input('Digite novamente a senha: '))
            else:
                break

        senha_cadastro_confirmacao = str(input('Digite novamente a senha: '))

        # Essa parte serve para caso o usuário digite senhas diferentes nos campos
        while senha_cadastro != senha_cadastro_confirmacao:
            print('As senhas não coincidem! Tente digite-las novamente.')
            senha_cadastro = str(input('Senha: '))
            senha_cadastro_confirmacao = str(input('Digite novamente a senha: '))

        celular_cadastro = str(input('Digite o número do seu celuar: ')).replace(" ", "")

        # Caso o usuário digite um número de celular fora dos padrões esperados
        while True:
            if len(celular_cadastro) != 11 or celular_cadastro.isalpha() is True:
                print('Número inválido! Digite o número novamente.')
                celular_cadastro = str(input('Digite o número do seu celuar: ')).replace(" ", "")
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
        os.system('clear')

        # Pergunta caso o usuário queira cadastrar o cartão de crédito agora ou não
        cadastrar_cartao_cadastro = str(input('Deseja cadastrar o seu cartão para facilitar futuras compras? [S/N] '))
        from time import sleep
        if cadastrar_cartao_cadastro == 'S':

            # Limpa o terminal
            os.system('clear')

            # Esse código serve para cadastrar um cartão de crédito
            print('-=' * 5, 'Cadastro Cartão', '-=' * 5)
            numero_cartao = str(input('Insira o número do cartão: ')).replace(" ", "")

            # Aqui se verifica se o cartão tem dezesseis dígitos como o esperado
            contador_numero_cartao = 0
            while True:
                for contador_numero_cartao in range(len(numero_cartao)):
                    contador_numero_cartao += 1
                if contador_numero_cartao != 16:
                    print('Número de digitos inválido!')
                    numero_cartao = str(input('Insira o número do cartão novamente: ')).replace(" ", "")
                else:
                    break

            titular_cartao = str(input('Insira o nome do titular: ')).upper()
            validade_cartao = str(input('Insira a data de validade do cartão (mm/aa): ')).replace("//", " ")

            # Verificado se o usuário digitou apenhas números e se foi no padrão solicitado
            while True:
                if validade_cartao.isalnum() is True:
                    print('Validade do cartão inválida. Tente novamente')
                    validade_cartao = str(input('Insira a data de validade do cartão novamente (mm/aa): ')).replace(
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
                    print('Código de segurança inválido! Tente digita-lo novamente.')
                    codigo_seguranca_cartao = str(input('Digite o código de segurança do cartão: '))
                elif codigo_seguranca_cartao.isalpha() is True:
                    print('Código de segurança inválido! Tente digita-lo novamente.')
                    codigo_seguranca_cartao = str(input('Digite o código de segurança do cartão: '))
                else:
                    break

        # Limpa o terminal
        os.system('clear')

        print('Redirecionando para a tela inicial...')
        sleep(5)

        break

    # Se o usuário na hora de escolher se logar ou se cadastrar digitar uma opção inválida, essa mensagem aqui aparece
    print('Opção inválida! Tente novamente:')
    opcao_entrada = input(str('Opção: '))
