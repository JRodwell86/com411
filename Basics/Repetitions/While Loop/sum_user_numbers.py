#ask user for a number
sum = int(input("How many numbers should I sum up?"))

summed = 0
print()

#total of numbers
total = 0

while summed < sum:
    print(f"Please enter number {summed} of {sum}")
    number = int(input())
    total = total + number
    summed = summed + 1

print(f"The answer is {total}")
