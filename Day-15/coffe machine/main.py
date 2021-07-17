from art import *
from data import *
import os
def clear(): return os.system('cls')


def report_resources():
    print(resources_art)
    for resource, amount in resources.items():
        print("{}: {}".format(resource, amount))


def report_menu():
    print(menu_art)
    for coffee, info in MENU.items():
        print("{} ${:.2f}".format(coffee, info["cost"]))


def report_ingredients(coffee):
    report_resources()
    print(f"Ingredients needed for {coffee} :")
    print(MENU[coffee]["ingredients"])


def report_money():
    print(money_art)
    print("Total amount in machine :${:.2f}".format(money_in_machine))


def modify_machine_resources(resources_needed, type):
    '''modifies resources in machine'''
    global resources

    if type == "add":
        for resource, amount in resources_needed.items():
            resources[resource] += int(amount)
        return True
    elif type == "remove":
        for resource, amount in resources_needed.items():
            resources[resource] -= int(amount)
        return True
    else:
        print(f"Invalid type in {type}ing resources")

    return False


def modify_machine_money(money, method):
    '''modifies money in machine'''
    global money_in_machine
    money_withdrawn = 0

    if method == "add":
        money_in_machine += money
        return True, 0
    elif method == "withdraw":
        if money_in_machine >= money:
            money_withdrawn = money_in_machine - money
            return True, money_withdrawn
        else:
            money_withdrawn = money_in_machine
            money_in_machine = 0
            return True, money_withdrawn
    else:
        print("Invalid method to money operations")


def receive_money(product):
    '''calculates money operations'''
    money_required = float(MENU[product]["cost"])
    money_paid = 0

    while True:
        if input("Add money ? (y/n) ").lower() == "y":
            money_paid += float(input("Enter amount :"))
            if money_paid < money_required:
                print("Not enough money")
            elif money_paid >= money_required:
                print(f"Payment received {money_paid}")
                balance = money_paid - money_required
                total_bill = money_paid - balance
                if balance > 0:
                    print("Here is your balance: ${:.2f}".format(balance))

                modify_machine_money(total_bill, "add")
                return True, 0
        else:
            return False, money_paid


def make_coffee(coffee):
    '''makes a coffee'''
    resources_required = MENU[coffee]["ingredients"]
    resources_available = resources.copy()

    for item, amount in resources_required.items():
        if resources_available[item] < amount:
            report_ingredients(coffee)
            print(f"Not enough {item}")
            return False, MENU[coffee]["cost"]

    modify_machine_resources(resources_required, "remove")
    return True, 0


def manage_machine():
    '''modify resources of machine'''
    choice = input(
        "What do you want to modify in machine (money /resources) ? ").lower()

    if choice == "money":
        method = input(
            "How do you want to modify money ? (add / withdraw) ").lower()
        money = float(input("Enter amount : "))
        is_modified, money_withdrawn = modify_machine_money(money, method)

        if money_withdrawn:
            print("withdrawn amount {:.2f}".format(money_withdrawn))

    elif choice == "resources":
        water = input("How much water do you want to add ? ")
        coffee = input("How much coffee do you want to add ? ")
        milk = input("How much milk do you want to add ? ")

        is_modified = modify_machine_resources({
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }, "add")

    if is_modified:
        print(f"Machine modified {choice} updated")


def reset_screen():
    ''''resets screen'''
    clear()
    print(coffee_art)


def machine_on():
    '''main machine loop'''
    machine_running = True
    while machine_running:
        report_menu()
        instruction = input("What do you want to make? ").lower()
        if instruction == "off":
            reset_screen()
            print("Switching off ...")
            return
        elif instruction == "report":
            reset_screen()
            report_resources()
            report_menu()
            report_money()
            return
        elif instruction == "manage":
            reset_screen()
            manage_machine()
        else:
            if instruction in MENU:
                payment_received, refund = receive_money(instruction)
                if payment_received:
                    coffee_served, refund = make_coffee(instruction)

                    if coffee_served:
                        print(f"Have your{coffee_emoji} {instruction}")
                    else:
                        print(
                            f"Coffee is not made coz lack of res money refunded : {refund}")
                else:
                    print(
                        f"No money received cant make coffee, money refunded : {refund}")
            else:
                print("I don't understand")

        if input("Another coffee ? (y/n)").lower() == 'y':
            reset_screen()
        else:
            machine_running = False
            print("Goodbye")


while input("Want to use the coffee machine ? (y/n) : ").lower() == "y":
    reset_screen()
    machine_on()
