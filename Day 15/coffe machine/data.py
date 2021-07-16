import random

# menu items
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 50.6,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 75.2,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 80.5,
    }
}

resources = {
    "water": random.randint(100, 1000),
    "milk": random.randint(100, 1000),
    "coffee": random.randint(100, 1000),
}

money_in_machine = random.randint(0, 250)

coffee_emoji = "☕"