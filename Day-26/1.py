numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n ** 2 for n in numbers]

print(squared_numbers)

result = [n for n in numbers if n % 2 == 0]

print(result)