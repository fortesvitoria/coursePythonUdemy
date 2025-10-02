#TODO: write out the 4 functions + - / *

def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    if n2 == 0:
        print("You can't divide a number by zero!")
    return n1 / n2

#TODO: Add these 4 functions into a dictionary as the values. Keys = + - * /
#remeber not to trigger the functions with the (), because we're storing it, not using it
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#Function to deal with inputs that are not numbers
def get_number(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("You typed an invalid input. Please, type a number.")

#TODO: Use the dictionary operations to perform the calculations. Multiply 4*8 using the dictionary
#to access: call the name of the dictionary, add a set of [] with the key name, and pass the parameters inside a set of ()
#print(operations['*'](4,8))

'''
1. Program asks the user to type the first number
2. Program asks the user to type a mathematical operator (a choice of +,-,*,/)
3. Program asks the user to type the second number
4. Program works out the result based on the chosen mathematical operator
5. Program asks if the user wants to continue working with the previous result
6. If yes, program loops to use the previous result as the first number and then repeats the calculation process
7. If no, program asks the user for the first number again, and wipes all the memory of previous calculations 
'''

def calculator():
    n1 = get_number("Whats the first number?\n")

    while True:
        operator = input("Pick an operator: '+','-','*',/\n")

        if operator not in operations:
            print("Please, type a valid operator.")
            continue

        n2 = get_number("Whats the second number?\n")
        result = operations[operator](n1,n2)
        print(f"The result of {n1} {operator} {n2} is {result}.")

        choice = input(f"Type 'y' if you want to continue working with {result}, or type 'n' if you want to start a new calculation.\n")
        if choice.lower() == 'y':
            n1 = result
        elif choice.lower() == 'n':
            calculator()
        else:
            print("Invalid option. Please try again.")

calculator()
