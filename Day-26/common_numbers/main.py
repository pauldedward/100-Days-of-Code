
with open("./Day-26/common_numbers/file_1.txt") as file:
    array_one = file.readlines()
with open("./Day-26/common_numbers/file_2.txt") as file:
    array_two = file.readlines()

# result = [int(num) for num in array_one if num in array_two]
array_one = [int(x.strip()) for x in array_one]
array_two = [int(x.strip()) for x in array_two]

result = []
for x in array_one:
    if x in array_two:
        result.append(x)

print(result)