age = input("Enter your age : ")

weeksLeft = (90 * 52) - (int(age) * 52)
monthsLeft = (90 * 12) - (int(age) * 12)
daysLeft = (90 * 365) - (int(age) * 365)

print(
    f"You have {weeksLeft} weeks {monthsLeft} months {daysLeft} days to live")
