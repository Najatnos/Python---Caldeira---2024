def PulaLinha():
    print('\n')
def LimparTerminal():
    print("\033[H\033[J", end="")
def Encerrar():
    print('Finalizando o sistema')
def Cadastrar():
    print('Cadastrar restaurante')
def Listar():
    print('Listar restaurante')
def Ativar():
    print('Ativar restaurante')
def MostreNomeDoApp():
    print('''
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀''')
def MostreOpcoesRestaurante():
    print(f'\n 1. Cadastrar restaurante\n 2. Listar restaurante\n 3. Ativar restaurante\n 4. Sair\n')
def Decida():
    OpcaoEscolhida = int(input('Qual sua escolha? '))
    PulaLinha()
    if OpcaoEscolhida in [1, 2, 3]:
        print(f'Opção {OpcaoEscolhida} á caminho!'.format(OpcaoEscolhida = OpcaoEscolhida))
    PulaLinha()
    match OpcaoEscolhida:
        case 1:
            Cadastrar()
        case 2:
            Listar()
        case 3:
            Ativar()
        case 4:
            LimparTerminal()
            Encerrar()
        case _:
            print('Opção inválida!')
            Decida()

    #Inteiro = int(OpcaoEscolhida)
def main():
    
    MostreNomeDoApp()
    MostreOpcoesRestaurante()
    Decida()
if __name__ == '__main__':
    main()
