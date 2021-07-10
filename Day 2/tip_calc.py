bill = float(input("Enter bill : "))
tip = float(input("Percentage of tip [10, 12, 15] percentage : "))
person = int(input("Total persons: "))

tip_amount = bill * (tip/100)
total_bill = bill + tip_amount
bill_per_person = "{:.2f}".format(total_bill / person)

print(f"Total bill is : ${total_bill} and one should pay {bill_per_person}")
