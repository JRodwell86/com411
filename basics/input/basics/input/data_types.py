# Ask user to enter their name
name = input("What is your name human?")
print(f"It is nice to meet you human {name}")
# Ask user to enter their age
age = input("How old are you (in years)?")
Height =float(input("How tall are you (in metres)?"))
Weight =int(input("How much do you weigh (in kilograms)?"))
answer = Weight / Height **2
bmi = str(round(answer, 2))
print(f"{name} you are {age} years old and your bmi is {bmi}")

