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
    "money" : 0,
}

money = 0
coffe_machine = True #its ON

def is_resources_checker(ingridents):
    for item in ingridents:
         if ingridents[item] >= resources[item]:
             print(f"Sorry there is not enough {item}.")
            return False
    return True

def total_coins():
    print("Please insert coins")
    quarters = int(input("Enter the no.of quarters you put in: \t")) * 0.25
    dimes = int(input("Enter the no.of dimes you put in: \t")) * 0.1
    nickles = int(input("Enter the no.of nickles you put in: \t")) * 0.05
    pennies = int(input("Enter the no.of pennies you put in: \t")) * 0.01

    total = quarters + dimes + nickles + pennies
    return total

#check if user has enought money and get the man a drink

while coffe_machine:
    user_choice_drink = input(str("What would you like (espresso/latte/cappuccino):\t")).lower()
    if user_choice_drink == "off":
        coffe_machine = False
    elif user_choice_drink == "report":
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}g")
        print(f"Money : ${money}")
    else:
        drink = MENU[user_choice_drink]
        if is_resources_checker(drink):
            if user_choice_drink == "espresso":
                print()
            elif user_choice_drink == "latte":
                print()
            elif user_choice_drink == "cappuccino":
                print()


