scores = [150, 142, 155, 166, 178, 65, 88, 99, 77, 177, 168, 159, 225, 185]

#function sum
total_score = sum(scores)
print(f'Function sum from python: {total_score/len(scores):.2f}')

#sum function with lopping
def sum_score():
    sum = 0
    for score in scores:
        sum += score
    print(f'Function sum made with for loop: {sum/len(scores):.2f}')

sum_score()

print('-' * 20)

print('1) Replicate the MAX function:')
#shows the highest number
print(f'Function max from python: {max(scores)}')

def max_score():
    higher = 0
    for score in scores:
        if score > higher:
            higher = score
    print(f'Function max made with for loop: {higher}')

max_score()