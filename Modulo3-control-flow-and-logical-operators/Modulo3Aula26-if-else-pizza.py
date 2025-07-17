print(f'{ '*' * 7 } Welcome to the pizza delivery! { '*' * 7 }')
name = input('Type your name: ')
size = input('What size pizza do you want? S, M or L: ')
# S = 15, M = 20, L = 25
pepperoni = input('Do you wand pepperoni on your pizza? Y or N: ')
#S = 2, M OR L = 3
extra_cheese = input('Do you want extra cheese? Y or N: ')
# + 1
price = 0

#todo: work out how much they need to pay based on their choise.
#todo: work out how much to add to their bill bases on their pepperoni choice.
#todo: work out their fginal amound based on whether if they want extra cheese.

if size.upper() == 'S':
    price += 15
    if pepperoni.upper() == 'Y':
        price += 2

elif size.upper() == 'M':
    price += 20
    if pepperoni.upper() == 'Y':
        price += 3

elif size.upper() == 'L':
    price += 25
    if pepperoni.upper() == 'Y':
        price += 3

if extra_cheese.upper() == 'Y':
    price += 1

print(f'{name} you order a {size} pizza. With pepperoni? ({pepperoni}). With extra cheese? ({extra_cheese}).')
print(f'Your total bill is {price}')