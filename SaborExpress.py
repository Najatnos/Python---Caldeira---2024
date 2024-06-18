from unidecode import unidecode
import time
TipoBusca = None
Restaurantes = [{'Nome':'Subauru', 'Categoria':'Fast food', 'Cargo-chefe':'Bauru', 'Status':True},
                {'Nome':'MuyGuápo', 'Categoria':'Mexicana', 'Cargo-chefe':'Taco', 'Status':True},
                {'Nome':'IceIceBaby', 'Categoria':'Sorveteria', 'Cargo-chefe':'Açai', 'Status':False}]
def NeutralizadorAcento(texto):
    return unidecode(texto)
def Pula():
    r = input('\nVolte ao menu digitando "r": ')
    if r == 'r': print("\033[H\033[J", end=""), main()
    else: Encerrar()
def LimparTerminal():
    print("\033[H\033[J", end="")
def Encerrar():
    LimparTerminal()
    TituloDecisao('\033[1mFINALIZANDO O SISTEMA.\033[0m \n')
def Error():
    LimparTerminal()
    r = input('\nVolte ao menu digitando "r": ')
    if r == 'r': main()
    else: Encerrar()
def BuscaNome(NomeRestaurante, CatalogoRestaurante):
    NomeRestaurante = NeutralizadorAcento(NomeRestaurante.lower())  
    return next((Restaurante for Restaurante in CatalogoRestaurante if NeutralizadorAcento(Restaurante['Nome'].lower()) == NomeRestaurante), None)
    return Buscado
def TituloDecisao(titulo):
    print(titulo)
    print()
def Listar():
    LimparTerminal()
    TituloDecisao('\033[1mLISTAMENTO DE RESTAURANTES.\033[0m \n')
    print(f'{'NOME'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'CARGO-CHEFE'.ljust(20)} | STATUS')
    for Restaurante in Restaurantes:
        NomeRestaurante = Restaurante['Nome']
        CategoriaRestaurante = Restaurante['Categoria']
        CargoChefeRestaurante = Restaurante['Cargo-chefe']
        StatusRestaurante = 'Ativo' if Restaurante['Status'] else 'Inativo'
        print(f'• {NomeRestaurante.ljust(20)} - {CategoriaRestaurante.ljust(20)} - {CargoChefeRestaurante.ljust(20)} - {StatusRestaurante}')
    Pula()
def ProcuraNome(TipoBusca):
    while True:
        LimparTerminal()
        TituloDecisao('\033[1mPROCURANDO NOME.\033[0m \n')
        Busca = input("Digite o nome do restaurante: ")
        Buscado = BuscaNome(Busca, Restaurantes)
        if Buscado:
            print("O restaurante '{}' foi encontrado! (Espere cinco segundos)".format(Buscado['Nome']))
            if TipoBusca == 'Ativa/Desativa.': 
                time.sleep(5)
                LimparTerminal()
                AtivarDesativar(Buscado)
            break        
        else:
            print(f"O restaurante '{Busca}' não foi encontrado. Tente novamente nos próximos doze segundos.")
            time.sleep(12)
            LimparTerminal()
def AtivarDesativar(Restaurante):
    TituloDecisao('\033[1mATIVAR/DESATIVAR.\033[0m \n')
    Restaurante['Status'] = not Restaurante['Status']
    NovoStatus = "Ativo" if Restaurante['Status'] else "Inativo"
    print("Agora, o restaurante está: ", NovoStatus)
    Pula()
def Cadastrar():
    LimparTerminal()
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
    global TipoBusca
    try:
        OpcaoEscolhida = int(input('Qual sua escolha? '))
        if OpcaoEscolhida == 1:
                Cadastrar()
        elif OpcaoEscolhida == 2:
                Listar()
        elif OpcaoEscolhida == 3:
                TipoBusca = 'Ativa/Desativa.'
                ProcuraNome(TipoBusca)
        elif OpcaoEscolhida == 4:
                LimparTerminal()
                Encerrar()
        else :
                Error()
    except ValueError:
        Error()
    #Inteiro = int(OpcaoEscolhida)
def main():
    
    MostreNomeDoApp()
    MostreOpcoesRestaurante()
    Decida()
if __name__ == '__main__':
    main()
