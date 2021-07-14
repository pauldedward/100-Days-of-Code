
input = int(input("Enter a number: "))

def checkPrime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print("Not a prime number")
                return
        print("Prime number")
    elif number == 1:
        print("Neither prime nor not prime")
        return
    else:
        print("Not a prime number")
        return

checkPrime(input)