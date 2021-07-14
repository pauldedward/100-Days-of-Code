import math

height = int(input("Enter the height of the area: "))
width = int(input("Enter the width of the area: "))
coverage = 5

def calculate(height,width, coverage):
    return math.ceil((height * width) / coverage)

print(f"You need {calculate(height,width,coverage)} cans of paint.")