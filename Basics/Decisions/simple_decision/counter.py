#to work out the number of odd and even
first_number = int(input("Please the first whole number"))
second_number = int(input("Please the second whole number"))
third_number = int(input("Please the second whole number"))
even_number = 0
odd_number = 0
#work out even or odd
if first_number % 2 != 0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if (second_number % 2 != 0):
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if (third_number % 2 != 0):
    even_number = even_number + 1
else:
    odd_number = odd_number + 1

print(f"There are {odd_number} odd numbers and {even_number} even numbers ")


