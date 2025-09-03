from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("WELCOME TO DR. PALAZZO'S COFFEE MACHINE!")
print("Coins Available:\n"
      "quarters = $0.25 \ndimes = $0.10 \nnickles = $0.05 \npennies = $0.01 "
      )
print("MENU:\n"
      "Espresso: $1.5\n"
      "Latte: $2.5\n"
      "Cappuccino: $3.0")
print("INSTRUCTIONS:\n"
      "Type 'off' to shut down the machine.\n"
      "Type 'Report' to know the amount of resources available for your order.\n")

items = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user_choice_in_progress = True
while user_choice_in_progress:
   user_choice = input(f"What would you like? {items.get_items()}. Check the top for the cost of each:")
   if user_choice == "report":
       coffee_maker.report()
       money_machine.report()

   elif user_choice == "off":
       print("Shutting down complete!")
       user_choice_in_progress = False

   else:
       drink = items.find_drink(user_choice)
       if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
           coffee_maker.make_coffee(drink)

