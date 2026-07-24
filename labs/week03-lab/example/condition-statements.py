# Simple if statement
age = int(input("Enter your age: "))
if age >= 20:
    print("You are an adult")


# if-else statement
temperature = 26
if temperature > 35:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B+")
elif score >= 75:
    print("Grade: B")
elif score >= 70:
    print("Grade: C+")
elif score >= 65:
    print("Grade: C")
elif score >= 60:
    print("Grade: D+")
elif score >= 55:
    print("Grade: D")
else:
    print("Grade: F")
