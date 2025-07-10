'''
Exercicio baseado no diagrama - tickets montanha russa
'''

name = input('Welcome! Type your name: ')
height = float(input('Whats your height in cm? '))
bill = 0

if height >= 120:
    age = int(input(f'{name} whats your age? '))

    #até 12 anos
    if age <= 12:
        bill = 5
        print('Your ticket price is $5.')

    #de 12 a 18 anos
    elif age <= 18:
        bill = 7
        print('Your ticket price is $7.')

    #acima de 18 anis
    else:
        bill = 12
        print('Your ticket price is $12.')

    #quer foto
    wants_photo = input('Do yhou want to have a photo take? Type y or n: ')
    if wants_photo == 'y':
        bill = bill + 3

    print(f'Total price: {bill}')


else:
    print(f'Sorry {name}, you are too short to ride the rollercoaster!')
