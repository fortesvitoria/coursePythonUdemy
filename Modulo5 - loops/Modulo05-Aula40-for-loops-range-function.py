'''
for loops with range function

for number in range(a,b)
    print(number)
'''

print('Range function:')
for number in range (1,11, 2): #11 not included, jumps every 2 numbers
    print(number)

print('-' * 20)

print('Sum from 1 till 100: ')
def gauss_challenge():
    total = 0
    for i in range (1,101): #101 not included
        total += i
    print(f'The sum from 1 till 100 is {total} ')

gauss_challenge()