
bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("Normal")
elif bmi >= 25.0 and bmi < 30.0:
    print("Overweight")
else:
    print("Obese")
