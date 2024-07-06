import time
import os
Numbers = [2, 8, 15, 23, 91, 112, 256]
Enumerate = len(Numbers)

def Title():
    print('''
          
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░▄▀░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░████████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████
█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████
█████████░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░████████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
          ''')
    JumpIt()

def JumpIt():
    print()

def Cleanme():
    _ = os.system('cls')
def Titles(titles):
    print('\033[0;35;1;3m' + titles + '\033[0m')
    print()

def Stringdatas(stringdatas):
    print('\033[01;35;2;3m' + stringdatas + '\033[0m')
    print()

def Infodelivery(infodelivers):
    print('\033[1;37m ⓘ ' + infodelivers + '\033[0m')

def TryAgain():
    print('Just press numbers and valid ones. Try again.')
    time.sleep(3)
    Cleanme()

def Press():
    global Enumerate
    try:
        press = int(input(f'Choose one of the {Enumerate} options in numbers '
                          '(or choose "0" to return to menu): '))
        while press > Enumerate or press < 0:
            print('Just press numbers and valid ones. Try again.')
            press = int(input(f'Choose one of the {Enumerate} options in numbers '
                              '(or choose "0" to return to menu): '))
        return press
    except ValueError:
        print('Just press numbers and valid ones. Try again.')
        return Press()

def Pressdefault():
    pressdefault = input('Press "X" if you want it. ')
    return pressdefault.lower() == 'x'

def SawNumbers():
    print("Numbers - ", end=' ')
    for number in Numbers:
        print('\033[01;35;2;3m', number, '\033[0m', end=' ')
    JumpIt()

def Sawlist():
    Titles('Here are the numbers to use the square root formula:')
    for i in range(len(Numbers)):
        Stringdatas(f'{i+1}. {Numbers[i]}')

def ShowList():
    Sawlist()
    Infodelivery('You can add or delete a number from the list.')
    if Pressdefault():
        Cleanme()
        Shapenumbers()
    else:
        Cleanme()
        Title()
        Chooseme()

def Shapenumbers():
    global Enumerate
    Titles('Here are some ways to shape the numbers: ')
    JumpIt()
    for i in range(3):
        Enumerate = i + 1
        Shapeways = ['Add', 'Delete', 'Replace']
        Stringdatas(f'{i + 1}. {Shapeways[i]} number.')
    press = Press()
    if press == 0:
        Cleanme()
        Title()
        Chooseme()
    elif press == 1:
        Cleanme()
        Add()
    elif press == 2:
        Cleanme()
        Del()
    elif press == 3:
        Cleanme()
        Rpl()

def Add():
    SawNumbers()
    JumpIt()
    try:
        PutIn = float(input('Iterate the number to add: '))
        Numbers.append(PutIn)
        JumpIt()
        Titles('See your add: ')
        SawNumbers()
        JumpIt()
        Infodelivery('Would you like to add one more time?')
        if Pressdefault():
            Cleanme()
            Add()
        else:
            Cleanme()
            Shapenumbers()

    except ValueError:
        TryAgain()
        Add()

def Del():
    Sawlist()
    JumpIt()
    if len(Numbers) == 0:
        print('There is not a single number on the list.\nRedirecting to Shape Numbers canon.')
        Cleanme()
        Shapenumbers()
    else:
        try:
            PutOut = int(input('Iterate the index to delete: ')) - 1
            while PutOut < 0 or PutOut >= len(Numbers):
                TryAgain()
                Del()
            del Numbers[PutOut]
            JumpIt()
            Titles('See your delete: ')
            SawNumbers()
            JumpIt()
            Infodelivery('Would you like to delete one more time?')
            if Pressdefault():
                Cleanme()
                Del()
            else:
                Cleanme()
                Shapenumbers()

        except ValueError:
            TryAgain()
            Del()

def Rpl():
    Sawlist()
    JumpIt()
    if len(Numbers) == 0:
        print('There is not a single number on the list.\nRedirecting to Shape Numbers canon.')
        Cleanme()
        Shapenumbers()
    else:
        try:
            PutOn = int(input('Iterate the index to replace: ')) - 1
            while PutOn < 0 or PutOn >= len(Numbers):
                TryAgain()
                Rpl()
            Getthen = float(input('Iterate your number to replace: '))
            Numbers[PutOn] = Getthen
            JumpIt()
            Titles('See your replace: ')
            SawNumbers()
            JumpIt()
            Infodelivery('Would you like to replace one more time?')
            if Pressdefault():
                Cleanme()
                Rpl()
            else:
                Cleanme()
                Shapenumbers()

        except ValueError:
            TryAgain()
            Rpl()

def Chooseme():
    global Enumerate
    Titles('Here are some ways to do with the numbers: ')
    JumpIt()
    for i in range(3):
        Enumerate = i + 1
        Shapeways = ['Shape a List', 'Show a List', 'Decipher Square Root of a List']
        Stringdatas(f'{i + 1}. {Shapeways[i]} number.')
    press = Press()
    if press == 0:
        Cleanme()
        Title()
        Chooseme()
    elif press == 1:
        Cleanme()
        Shapenumbers()
    elif press == 2:
        Cleanme()
        ShowList()
    elif press == 3:
        Cleanme()
        SquareRoot()

def SquareRoot():
    SawNumbers()
    JumpIt()
    if len(Numbers) == 0:
        print('There is not a single number on the list.\nRedirecting to choose canon.')
        Cleanme()
        Title()
        Chooseme()
    else:
        for number in Numbers:
            Sqrl = number ** 0.5
            if Sqrl % 1 == 0:
                Sqrl = int(Sqrl)
            Titles(f'{number} with a {type(Sqrl).__name__} square root of: {Sqrl}.')
            JumpIt()
        Infodelivery('Would you like to repeat?')
        if Pressdefault():
            Cleanme()
            SquareRoot()
        else:
            Cleanme()
            Title()
            Chooseme()

def main():
    Title()
    Chooseme()

if __name__ == '__main__':
    main()
