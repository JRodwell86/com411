#ask user for a factorial number
factorial_number = int(input("Please enter a number"))
conditional = 0
total = 1
while conditional < factorial_number:
    conditional = conditional + 1
    total = total * conditional

print(f"The factorial is {total}")