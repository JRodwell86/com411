#checking for bigger or smaller numbers
first_number = int(input("Please the first number"))
second_number = int(input("Please the second number"))
if first_number < second_number:
    print("The first number is the smallest")
elif second_number < first_number:
    print("The second number is the smallest")
else:
    print("They are equal!")