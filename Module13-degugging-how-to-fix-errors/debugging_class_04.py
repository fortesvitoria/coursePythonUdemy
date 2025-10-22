'''
Fix the bug so that the print statement displays the correct value of age in the output area.

age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")
'''
while True:
    try:
        age = int(input("How old are you?\n"))
        break
    except ValueError:
        print("Please, type only numbers.")
        

if age > 18:
    print(f"You can drive at age {age}.") 
else:
    print(f"You CAN'T drive at age {age}.")

'''
How I fixed:
1. Ident the function prin() so it is inside the IF statement;
2. Add a 'f' before the string so it can read the variables.
3. Added an else, so it shows a message in case the age is bellow 18.
4. Add a while true with a try/except to catch errors
'''
