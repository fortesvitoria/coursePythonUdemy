'''
Asks the first number;
Asks the operator;
Asks the second number;
Shows the result
'''


def calculator():
    print("*** Welcome to the calculator! ***")

    n1 = float(input("\nType the first number: \n"))
    while True:
        operator = input("Which operation do you wanna do: Sum, Subtract, Multiply, or Divide?\n")
        if operator.lower() == "sum":
            result = n1 + float(input("Type the second number: \n"))
            break
        elif operator.lower() == "subtract":
            result = n1 - float(input("Type the second number: \n"))
            break
        elif operator.lower() == "multiply":
            result = n1 * float(input("Type the second number: \n"))
            break
        elif operator.lower() == "divide":
            n2 = float(input("Type the second number: "))
            if n2 == 0:
                return "Error: You can't divide a number by ZERO!"
            result = n1 / n2
            break
        else:
            print("Please, type a valid operation.")
    return result

show = calculator()

print(f"The result of your calculation is {show}")
