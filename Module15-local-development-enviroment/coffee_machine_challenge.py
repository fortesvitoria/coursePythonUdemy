'''
- 3 hot flavors: 
1 expresso - $1.5
50ml water
18g coffee

2 latte - $2.5
200ml water
24g coffee
150ml milk

3 cappucino - $3.0
250ml
24g coffee
100ml milk


- resources starts at:
300ml water
200ml milk
100g coffee

- coin operated:
penny - 1cent - 0.01
nickel - 5cents - 0.05
dime - 10cents - 0.10
quarter - 25cents 0.25

Program requirements 
1. print report;
2. check resources  sufficiente?
3. process coins
4. check if successful
5. make coffee

'''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

coin_value = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

# prints the key of dict, expresso, latter, etc
# print(list(MENU.keys())[1])

#prints the key and items of it: ('espresso', {'ingredients': {'water': 50, 'coffee': 18}, 'cost': 1.5})
# print(list(MENU.items())[0])

#print the keys only
# print(f"----------------------> {MENU['latte']}")

#deduct from water
# MENU['latte']['ingredients']['water'] -= 50
# print(f"2----------------------> {MENU['latte']}")

#deduct from resources
# resources["water"] -= 100
# print(resources["water"])


#PRINTS A REPORT
def display_report():
    print("--- AVAILABLE RESOURCES ---")
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")

on = True

def check_resources_sufficient(order_ingredients):
    """loop into the order ingredients, for each of the item in ingredients we will check if is greater or equal to those items in resources, returning true when the order can be made and false if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True
    
def process_coins():
    """Returns the total calculates from coins inserted"""
    print("Please insert coins:\n")
    total = int(input("How many quarters? \n")) * 0.25
    total += int(input("How many dimes? \n")) * 0.1
    total += int(input("How many quarters? \n")) * 0.05
    total += int(input("How many pennies? \n")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    """receive money and dirnk ocst, check if enough. If enoght, return true, add the coffe money to the cashier(profit), else, return a show a message and return False"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else: 
        print("Sorry, not enought money. Money refounded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Dedect the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is yhour drink {drink_name}")



while on:
    choice = input("“What would you like? (espresso/latte/cappuccino):\n").lower()

    if choice == "off":
        print("Turning the machine off...")
        on = False

    elif choice == "report":
        display_report()
    
    else:
        drink = MENU[choice]
        print(drink)
        if check_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

