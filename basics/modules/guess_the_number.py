
def play_guess_the_number():

    from random import randrange

    print("Please enter the minimum value")
    min_value = int(input())

    print("Please enter the maximum value")
    max_value = int(input())

    number = (randrange(min_value, max_value, 1))

    print(f"I am thinking of a number between {min_value} and {max_value}. Can you guess what it is?")
    guess = int(input())

    while guess < number:
        print("Your guess is too low")
        print("Try again")
        guess = int(input())

    while guess > number:
        print("Your guess is too high")
        print("Try again")
        guess = int(input())

    if guess == number:
        print("Congratulations! You guessed my number!")


if __name__ == "main":
    play_guess_the_number()
