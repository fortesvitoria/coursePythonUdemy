from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
        menu = Menu()
        coffee = CoffeeMaker()
        money = MoneyMachine()

        on = True 
        
        while on:
            choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

            if choice == "off":
                print("Turning the machine off...")
                on = False

            elif choice == "report":
                coffee.report()
                money.report()
            
            else:
                drink = menu.find_drink(choice)
                if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                        coffee.make_coffee(drink)

# Programa principal
if __name__ == "__main__":
    main()