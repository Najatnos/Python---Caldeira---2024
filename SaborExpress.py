from unidecode import unidecode
Restaurantes = [{'Nome':'Subauru', 'Categoria':'Fast food', 'Cargo-chefe':'Bauru', 'Status':True},
                {'Nome':'MuyGuápo', 'Categoria':'Mexicana', 'Cargo-chefe':'Taco', 'Status':True},
                {'Nome':'Ice, Ice Baby!', 'Categoria':'Sorveteria', 'Cargo-chefe':'Açai', 'Status':False}]
def NeutralizadorAcento(texto):
    return unidecode(texto)
def Pula():
    r = input('Volte ao menu digitando "r": ')
    if r == 'r': print("\033[H\033[J", end=""), main()
    else: Encerrar()
def LimparTerminal():
    print("\033[H\033[J", end="")
def Encerrar():
    TituloDecisao('\033[1mFINALIZANDO O SISTEMA.\033[0m \n')
def Error():
    print("\033[H\033[J", end="")
    r = input('Volte ao menu digitando "r": ')
    if r == 'r': main()
    else: Encerrar()
def BuscaNome(NomeRestaurante, CatalogoRestaurante):
    NomeRestaurante = NeutralizadorAcento(NomeRestaurante.lower())  
    return next((Restaurante['Nome'] for Restaurante in CatalogoRestaurante if NeutralizadorAcento(Restaurante['Nome'].lower()) == NomeRestaurante), None)
def TituloDecisao(titulo):
    print("\033[H\033[J", end="")
    print(titulo)
    print()
def Listar():
    TituloDecisao('\033[1mLISTAMENTO DE RESTAURANTES.\033[0m \n')
    for Restaurante in Restaurantes:
        NomeRestaurante = Restaurante['Nome']
        CategoriaRestaurante = Restaurante['Categoria']
        CargoChefeRestaurante = Restaurante['Cargo-chefe']
        StatusRestaurante = Restaurante['Status']
        print(f'• {NomeRestaurante} - {CategoriaRestaurante} - {CargoChefeRestaurante} - {StatusRestaurante}')
        print
    Pula()
def AtivarDesativar():
    print('Ativar restaurante')
def Cadastrar():
    TituloDecisao('\033[1mCADASTRO DE RESTAURANTES.\033[0m \n')
    RestauranteNome = input('Nome: ')
    while len(RestauranteNome) == 0: RestauranteNome = input('Não digitaste. Tente novamente. \nNome: ')
    Categoria = input('Categoria: ')
    while len(Categoria) == 0: Categoria = input('Não digitaste. Tente novamente. \nCategoria: ')
    CargoChefe = input('Cargo-chefe: ')
    while len(CargoChefe) == 0: CargoChefe = input('Não digitaste. Tente novamente. \nCargo-chefe: ')
    RestauranteDados = {'Nome':RestauranteNome, 'Categoria':Categoria, 'Cargo-chefe':CargoChefe, 'Status':False}
    Restaurantes.append(RestauranteDados)
    print(f'O restaurante {RestauranteNome} venderá {CargoChefe} de maneira próspera. A Sabor Express deseja tudo de bom ao seu negócio!')
    Pula()
def MostreNomeDoApp():
    print('''
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀''')
def MostreOpcoesRestaurante():
    print(f'\n 1. Cadastrar restaurante\n 2. Listar restaurante\n 3. Ativar restaurante\n 4. Sair\n')
def Decida():
    try:
        OpcaoEscolhida = int(input('Qual sua escolha? '))
        if OpcaoEscolhida in [1, 2, 3]:
            print(f'\nOpção {OpcaoEscolhida} á caminho!'.format(OpcaoEscolhida = OpcaoEscolhida))
        match OpcaoEscolhida:
            case 1:
                Cadastrar()
            case 2:
                Listar()
            case 3:
                AtivarDesativar()
            case 4:
                LimparTerminal()
                Encerrar()
            case _:
                Error()
    except:
        Error()
    #Inteiro = int(OpcaoEscolhida)
def main():
    
    MostreNomeDoApp()
    MostreOpcoesRestaurante()
    Decida()
if __name__ == '__main__':
    main()
