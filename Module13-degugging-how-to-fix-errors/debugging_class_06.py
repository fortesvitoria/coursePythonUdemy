'''
PAUSE 1
Use the PyCharm debugger to figure out what is the issue in the starting code and fix it.

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
'''
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item) #solution: ident here, so the append is inside the for loop
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])