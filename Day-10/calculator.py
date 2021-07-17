import os
def clear(): return os.system('cls')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():

    clear()
    print("Welcome to the calculator!")
    should_continue = True
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    while should_continue:

        symbol = input("Enter the operation: \n+\n-\n*\n/\n")
        calculate_function = operations.get(symbol)

        answer = calculate_function(first_number, second_number)
        print(f"{first_number} {symbol} {second_number} = {answer}")

        if input(f"calculate with {answer} again? (y/n) ") == "y":
            clear()
            first_number = answer
            print(f"Previousanswer: {first_number}")
            second_number = float(input("Enter the number: "))
        else:
            should_continue = False
            calculator()


calculator()
