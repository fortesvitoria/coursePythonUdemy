'''
Prime Number Checker
Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  

1. You need to write a function called is_prime() 
2.that checks whether if the number passed into it is a prime number or not.  
3. It should return True or False.

e.g.

7 is a primer number because it is only divisible by 1 and itself.
But 4 is not a prime number because you can divide it by 1, 2 or 4.

NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

Example Input 1
73
Example Output 1
True


Example Input 2
75
Example Output 2
False
'''

def is_prime(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        return False
    
    # Check for divisors from 2 up to the number before num
    # If we find any divisor, it's not a prime number
    for i in range(2, num):
        if num % i == 0:
            return False
            
    # If the loop completes without finding any divisors, the number is prime
    return True

result = is_prime(75)
print(result)

result1 = is_prime(73)
print(result1)

