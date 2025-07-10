'''
Exercicio baseado no diagrama - tickets montanha russa
'''

name = input('Welcome! Type your name: ')
height = float(input('Whats your height in cm? '))
price = 0
photoadd = 3
totalprice = 0

if height < 120:
    print(f'Sorry {name}, you are too short to ride the rollercoaster!')
else:
    age = int(input(f'{name} whats your age? '))
    #até 12 anos
    if age < 12:
       price = 5
       totalprice = price

    #de 12 a 18 anos
    elif age > 12 and age < 18:
        price = 7
        totalprice = price

    #acima de 18 anos
    elif age > 18:
        price = 12
        totalprice = price

    photo = input(f'Your ticket price is ${price}. Do you wanna photos for ${photoadd}? Types Y for yes and N for no: ')
    if photo.upper() == 'N':
        print(
            f'{name} you are {age} years old, ticket price is ${price} and dont want a photo. Your total bill is ${totalprice}.')
    elif photo.upper() == 'Y':
        totalprice = photoadd + price
        print(
            f'{name} you are {age} years old, ticket price is ${price} and want a photo + ${photoadd}. Your total bill is ${totalprice}.')

