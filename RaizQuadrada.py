Numbers = [2, 8, 15, 23, 91, 112, 256]
# Changeable list of numbers

def Cleanme():
    print("\033[H\033[J", end="")

def Titles(titles):
    print('\033[0;35;1;3m'+titles)
    print()
# Facilitar a implementação da 
# marcação de títulos

def Stringdatas(stringdatas):
    print('\033[01;35;2;3m'+stringdatas)
    print()
# Facilitar a implementação da
# impressão de listas

def Infodelivery(infodelivers):
    print('\033[1;37m ⓘ '+infodelivers)
# Facilitar a implementação da 
# marcação de escolha rápida

def Press():
    global Enumerate
    try:
        press = int(input(f'Chose one of the {Enumerate}\ 
                          options in numbers\
                          (or choose "0" to return to menu): '))
        while press > Enumerate or press < 0:
            print('Try again.\n')
            Press()
        if 0 < press <= Enumerate:
            Cleanme()
        elif press == 0:
            Cleanme()
            Chooseme()  
    except:
        print('Just press numbers. Try again.\n')
        Press()
# Corpo padrão de um jogo de escolhas

    
def Pressdefault():
    pressdefault = input('Press "X" if you want it. ')
    if pressdefault.lower() == 'x':
        return True
    else:
        return False 
# Escolha rápida

def SawNumbers():
    Titles('Here are the numbers to use\
            the square root formula:')
    for i in range(Numbers):
        Stringdatas(f'{Numbers[i]}')
    Infodelivery('You can add or delete a number\
                  from the list.')
    pressdefault = Pressdefault()
    if pressdefault == True:
        Cleanme()
        Shapenumbers()
    else:
        Cleanme()
        Chooseme()
# Listar números

def Shapenumbers():
    global Enumerate
    Titles('Here are some ways to shape the numbers: ')
    for i in range(3):
        Enumerate = i
        Shapeways = ['Add','Delete','Replace']
        Stringdatas(f'{i + 1}. {Shapeways[i]} number. ')
    press = Press()
    match press:
        case 1: Add()
        case 2: Del()
        case 3: Rpl()
# Cânon da


    
    
    

