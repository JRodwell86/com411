#ask user for how many numbers to add up
number = int(input("Please enter a number"))
conditional = 0
total= 0
#ask user to enter numbers
while conditional < number:
    print(f"Please enter number {conditional} of {number}")
    user_number = int(input())
    total = total + user_number
    conditional = conditional + 1
    #print the total
print(f"{total}")