import random
RPS = ['Rock','Paper','Scissors']
machine = random.choice(RPS)
# print(machine)

print('Your options:')
print('1. Rock')
print('2. Paper')
print('3. Scissors')

try:
    you = int(input('Make your keyboard sing, boy: '))
    you = RPS[you - 1]
except:
    while type(you) == str:
         you = int(input('Make your keyboard sing, boy: '))

print(you)

victory = {
    'Rock':'Scissors',
    'Scissors':'Paper',
    'Paper':'Rock'
}

if you == machine:
    print('DRAW')
elif victory[you] == machine:
    print('WIN')
else:
    print('LOST')

print(f'{you} vs {machine}')
