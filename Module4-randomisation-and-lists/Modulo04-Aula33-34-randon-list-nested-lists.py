import random

print('Lets see hows gonna pay the bill!')

friends = ['Ana','Clara','Marco']

index = random.randint(0, len(friends) - 1)

print(f'{friends[index]} is going to pay the ALL bill!')

print(15 * '*')
print('Solved by Angela:')

print(random.choice(friends))

print(15 * '*')
print('Nesting:')

frutas = ['Morango', 'Abacaxi', 'Mamão']
vegetais = ['Pimentão', 'Pepino', 'Alface', 'Cenoura', 'Beterraba', 'Couve', 'Tomate']

mais_venenosos = [frutas,vegetais]

print(mais_venenosos)
print(mais_venenosos[1])
print(mais_venenosos[1][1])