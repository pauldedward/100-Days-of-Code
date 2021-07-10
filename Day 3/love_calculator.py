name1 = input("Enter your name : ")

name2 = input("Enter your partner's name : ")

name = name1 + name2
name.lower()

firstDigit = name.count("t")
firstDigit += name.count("r")
firstDigit += name.count("u")
firstDigit += name.count("e")

secondDigit = name.count("l")
secondDigit += name.count("o")
secondDigit += name.count("v")
secondDigit += name.count("e")

print(f"love percentage : {str(firstDigit) + str(secondDigit)}")
