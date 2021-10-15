from random import randrange

print("Please enter the minimum value")
mini = int(input())

print("Please enter the maximum value")
maxi = int(input())

range = (randrange(mini, maxi, 1))


print(f"I am thinking of a number between {mini} and {maxi}. Can you guess what it is?")
guess = int(input())

while guess < range:
    print("Your guess is too low")
    print("Try again")

while guess > range:
    print("Your guess is too high")
    print("Try again")

while guess == range:
    print("You did it!")