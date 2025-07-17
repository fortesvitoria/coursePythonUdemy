#importa biblioteca ramdom
import random

'''
RANDOM INTEGER
random.randint (a,b)
Return a random integer N such that a <= N <=b. Alias for randrand(a,b+1) 
inclusive of a and b
'''
random_int = random.randint (1,10)
print(f'Random integer: {random_int}')

'''
RANDOM FLOAT 1
random.random ()
Return the next random floating point number in the range 0.0 <= X <1.0
0 included, 1 not includes
'''

random_ran = random.random () * 10
print(f'Random float 1: {random_ran}')

'''
RANDOM FLOAT 2
random.uniform (a,b)
Return a random floating point numver N such that a <= N <= b for a <= b and b <= N <= a for b < a.
inclusive of a and b
'''

random_float = random.uniform (1,10)
print(f'Random float 2: {random_float}')

#EXERCICIO
print('*' * 15)
print('Exercicio: Se sair os números 5,7,8 = Heads, otherwise = Tails')

number = random.randint (1,10)

if number == 5 or number == 7 or number == 8:
    print(f'Heads! Number: {number}')
else:
    print(f'Tails! Number: {number}')