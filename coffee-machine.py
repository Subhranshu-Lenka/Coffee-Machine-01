# coffee machine program

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

profit_money = 0.00


def profit(gains):
    """Adds the profit to total earnings"""
    global profit_money
    profit_money += gains


def charge_coins(user_input):
    """Calculate total amount, keeps profit and returns the balance"""
    # quater,dime,nickel,penny
    quater = int(input("How many quaters?      "))*0.25
    dime = int(input("How many dimes?        "))*0.1
    nickel = int(input("How many nickels?      "))*0.05
    penny = int(input("How many pennies?      "))*0.01

    total = penny+nickel+dime+quater

    if total >= MENU[user_input]['cost']:
        change = total-MENU[user_input]['cost']
        profit(total-change)
        return change
    else:
        return ("fuck off")


def check_resourses_available(user_input):
    """Returns True when ingredients are sufficient else returns False"""
    for i in MENU[user_input]['ingredients']:
        if resources[i] < MENU[user_input]['ingredients'][i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def make_coffee(user_input):
    """Subtract the required amount of ingedients from resources to make the coffee."""
    for i in MENU[user_input]['ingredients']:
        resources[i] -= MENU[user_input]['ingredients'][i]


def refill(resouces):
    """Refill all the resources to 500g each"""
    for i in resources:
        resources[i] = 500


loop = True
# program execution

while(loop):
    user_input = input(
        "What would you like to have (Espresso/Latte/Cappuccino)     ").lower()

    if(user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino'):
        if check_resourses_available(user_input):
            payment = charge_coins(user_input)
            if payment != 'fuck off':
                make_coffee(user_input)
                print(f"Here is ${round(payment,2)} dollars in change")
                print(f"Here is your {user_input.title()}☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif(user_input == 'report'):
        print(
            f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nProfit:{profit_money}")
    elif(user_input == 'off'):
        loop = False
    elif(user_input == 'refill'):
        refill(resources)
    else:
        print("Please humans, it's just a coffee machine")
