day_of_week = input("Enter the day of week: ").lower()
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("Learn DevOps")
else:
    print("Practice DevOps")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
choice = input("Enter the operation: (Option +, -, *, /, %) ")
if choice == "+":
    print(num1+num2)
elif choice == "-":
    print(num1 - num2)
elif choice == "*":
    print(num1 * num2)
elif choice == "/":
    print(num1 / num2)
elif choice == "%":
    print(num1 % num2)
else:
    print("Please enter a valid option...")

age = 20
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")