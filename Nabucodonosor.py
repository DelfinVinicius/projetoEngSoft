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

# Área de login ou cadastro
while True:
    # Essa é a parte do login
    if opcao_entrada in 'LoginloginLOGIN':
        print('-=' * 10, 'LOGIN', '=-' * 10)
        login_login = str(input('Email: '))
        senha_login = int(input('Senha: '))
        break

    # Aqui é a do cadastro
    elif opcao_entrada in 'CadastrocadastroCADASTRO':
        print('-=' * 9, 'CADASTRO', '=-' * 9)
        print('Preencha os campos a seguir com as informações requisitadas!')
        login_cadastro = str(input('Informe o seu email: '))
        senha_cadastro = int(input('Crie uma senha com oito ou mais números: '))
        senha_cadastro_confirmacao = int(input('Digite novamente a senha criada a pouco: '))
        celular_cadastro = str(input('Digite o número do seu celuar: ')).replace(" ", "")
        # Caso o usuário digite um número de celular fora dos padrões esperados
        while len(celular_cadastro) < 11 or len(celular_cadastro) > 11:
            print('Número inválido! Tente inserir o DDD ou o "9" logo após o mesmo.')
            celular_cadastro = str(input('Digite o número do seu celuar: ')).replace(" ", "")
        # Descobrindo a região que o usuário provavelmente mora
        DDD = celular_cadastro[0] + celular_cadastro[1]
        if DDD in lista_DDDs:
            c = 0
            for i in lista_DDDs:
                if i == DDD:
                    regiao = lista_cidades_DDDs[c]
                c += 1

        # Essa parte serve para caso o usuário digite senhas diferentes nos campos
        while senha_cadastro != senha_cadastro_confirmacao:
            print('As senhas não coincidem! Tente digite-las novamente.')
            senha_cadastro = int(input('Senha: '))
            senha_cadastro_confirmacao = int(input('Digite novamente a senha: '))
        break

    # Se o usuário na hora de escolher se logar ou se cadastrar digitar uma opção inválida, essa mensagem aqui aparece
    print('Opção inválida! Tente novamente:')
    opcao_entrada = input(str('Opção: '))
