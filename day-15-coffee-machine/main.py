from typing import Match


menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

accepted_coins = {
    "2e": 2.0,
    "1e": 1.0,
    "50c": 0.5,
    "20c": 0.2,
    "10c": 0.1
}


def check_resources(choice_ingredients):
    for ingredient in choice_ingredients:
        if choice_ingredients[ingredient] >= resources[ingredient]:
            print("There is not enough " + str(ingredient))
            return False
    return True


def process_coins(cost):
    global profit
    inserted_value = 0
    print("\nThe cost of the selected option is " + str(cost) + " €")
    print("The machine accepts the following coins:")
    
    for coin_name in accepted_coins:
        print(coin_name, end=" ")
    print("\n")
    
    while inserted_value < cost:
        coin = input("Insert coin or 'cancel' your order: ")
        
        if coin in accepted_coins:
            coin_value = accepted_coins[coin]
            inserted_value += coin_value
            print("Current value of inserted coins: " + str(round(inserted_value, 1)))
        elif coin == "cancel":
            print("You cancelled your order... Returning " + str(round(inserted_value, 1) ) + " €...")
            return False
        else:
            print("Coin not accepted. Returning coin...")

    print("Inserted " + str(round(inserted_value, 1)) + " €. Returning " + str(round(inserted_value - cost, 1)) + " €...")
    profit += cost
    return True


def make_drink(choice_ingredients):    
    for ingredient in choice_ingredients:
        resources[ingredient] -= choice_ingredients[ingredient]
        
    print("Enjoy your drink. :)")
    
    return True


profit = 0.0
machine_on = True
options_menu = [*menu]
# options_menu = list(menu.keys())

while machine_on:
    print("\nCurrent menu options are:")
    for option in options_menu:
        print("- " + str(option))
    choice = input("What would you like? ")

    if choice == "off":
        machine_on = False
        print("Coffee machine is turning off...")
    elif choice == "report":
        for resource in resources:
            print(str(resource.capitalize()) + ":\t" +
                  str(resources[resource]) + " units")
        print("PROFIT: " + str(profit) + " €")
    elif choice in options_menu:
        choice_details = menu[choice]
        choice_ingredients = choice_details["ingredients"]
        cost = choice_details["cost"]

        if check_resources(choice_ingredients):
            if process_coins(cost):
                make_drink(choice_ingredients)