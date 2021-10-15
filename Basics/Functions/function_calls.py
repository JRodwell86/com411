def input_word():
    print("Please enter a word")
    word = input()
    print("Please select an option one-five")
    option = int(input())
    if option == 1:
        display_box(word)
    elif option == 2:
        lower_case(word)
    elif option == 3:
        upper_case(word)
    elif option == 4:
        reverse(word)
    elif option == 5:
        repeat(word)
    else:
        print("ERROR!!")

# function for ascii box
def display_box(word):
  message = f"* {word} *"
  print("*" * len(message))
  print(message)
  print("*" * len(message))

# function for lower
def lower_case(word):
    print(word.lower())

# function for upper
def upper_case(word):
    print(word.upper())

# function for reversed
def reverse(word):
        for position in range(len(word) - 1, -1, -1):
            print(word[position], end="")

#function for repetition
def repeat(word):
    print("\nHow many times would you like to repeat?")
    number = int(input())
    print(word * number)


input_word()

