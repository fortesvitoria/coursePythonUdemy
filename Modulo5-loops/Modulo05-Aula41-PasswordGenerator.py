import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+',
           '[',']','{','}','|',';',':',',','.','<','>','?','/']

password = []

pass_string_easy = ''

pass_string = ''


print('Welcome to the Password Generator!')
nr_letters = int(input('How many letters would you like on your password? '))
nr_numbers = int(input('How many numbers would you like on your password? '))
nr_symbols = int(input('How many symbols would you like on your password? '))

print(f'{'*'*10}EASY VERSION{'*'*10}\n')

for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

for char in password:
    pass_string_easy += char

print(f'Sua senha fraca é: {pass_string_easy}')


print(f'\n {'*'*10}HARD VERSION{'*'*10}\n')

random.shuffle(password)

for char in password:
    pass_string += char

print(f'Sua senha forte é: {pass_string}')