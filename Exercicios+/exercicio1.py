import hashlib
def Intro1():
    print('\nAntes, crie um nome de usuário e uma senha.')

def Intro2():
    print('\nAgora, digite sua idade.')

def Intro3():
    print('\nPor último, digite as coordenadas (X, Y) de onde você mora.')

def Atencao1():
    print('\033[31;1mAtenção:\033[0m' + ' \033[34;4mO nome de usuário necessita ter mais que três carácteres e não deve possuir números, assim como a senha deve ter no minímo cinco carácteres com ao menos um número!\033[0m')

def Erro():
    print('\033[31;1mOperação inválida:\033[0m' + ' \033[34;4mRepita.\033[0m')

def Erro2():
    print('\033[31;1mOperação Inválida:\033[0m' + ' \033[34;4mSó serão permitidos números. Repita.\033[0m')

def Titulo():
    print('''
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░████████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░▄▀░░████░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████''')

def Subtitulo():
    print('ＦＡＲＥＩ ＵＭ ＲＥＳＵＭＯ ＳＯＢＲＥ ＶＯＣＥ\n')

    

def main():
    
    Titulo()
    Subtitulo()
    Intro1()
    Atencao1()

  #exercicio número 3
    Nome = input('\nNome: ')
    while any(caractere.isdigit() for caractere in Nome) or len(Nome) <= 3:
        Erro()
        Atencao1()
        Nome = input('\nNome: ')
    Senha = input('\nSenha: ')
    while not any(caractere.isdigit() for caractere in Senha) or len(Senha) < 5:
        Erro()
        Atencao1()
        Senha = input('\nSenha: ')
   ###
  
    Intro2()
    Idade = input('\nIdade: ')
    while not all(caractere.isdigit() for caractere in Idade):
        Erro2()
        Idade = input('\nIdade: ')
      
  #exercicio número 2      
    if int(Idade) >= 0: age = 'Criança'
    if int(Idade) >= 13: age = 'Adolescente'
    if int(Idade) >= 18: age = 'Adulto'
  ###
  
  #exercicio número 1
    if int(Idade) & 1 == 0: parim = 'par'  
    else: parim = 'impar'
  ###
  
    Intro3()

  #exercicio número 4
    CoordenadaX = input('Coordenada X: ')
    CoordenadaY = input('Coordenada Y: ')
    if int(CoordenadaX) > 0 < int(CoordenadaY): PlanoCartesiano = 'Primeiro Quadrante'
    if int(CoordenadaX) < 0 < int(CoordenadaY): PlanoCartesiano = 'Segundo Quadrante'
    if int(CoordenadaX) < 0 > int(CoordenadaY): PlanoCartesiano = 'Terceiro Quadrante'
    if int(CoordenadaX) > 0 > int(CoordenadaY): PlanoCartesiano = 'Quarto Quadrante'
    else: PlanoCartesiano = 'Caso Contrário'
  ###
    CriptoSenha = hashlib.md5(Senha.encode()).hexdigest()
    print(f'\n\nTu és {Nome} da suposta senha "{CriptoSenha}", atualmente tens {Idade} anos de seu nome, um(a) {age}, claro(s) algarismo(s) {parim}, e caso vivesse em um plano cartesiano, estaria no {PlanoCartesiano}!')
if __name__ == '__main__':
    main()
