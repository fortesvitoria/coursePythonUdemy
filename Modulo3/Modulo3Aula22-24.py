#AULA22 e AULA24
name = input('Digite seu nome: ')
idade = int(input(f'{name} digite sua idade: '))
height = int(input(f'{name} digite sua altura em cm: '))

if height < 120:
    print('You are too short for the rollercoaster!')
else:
    print('Go ahead!')
    if idade < 12:
        print(f'{name} you are {idade} years old. Your ticket price is $ 5.')
    elif idade >= 12 and idade <= 18:
        print(f'{name} you are {idade} years old. Your ticket price is $ 7.')
    else:
        print(f'{name} you are {idade} years old. Your ticket price is $ 12.')


print('---------------------------')
#AULA23 MODULO
modulo = 10%3
print(modulo)
print('---------------------------')
print('Check if the number ir odd or even:')
n = int(input('Digite um número inteiro: '))
module = n%2

if module == 0:
    print(f'The numer {n} is even! Modulo: {module}.')
else:
    print(f'The number {n}   is odd! Modulo: {module}.')