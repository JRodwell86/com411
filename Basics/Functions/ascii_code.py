print("Program Started...")
# input standard character
character = input("Please enter a standard character")
value = ord(character)
# count letters in character
letter = len(character)
# output ascii code or error message
if letter == 1:
    print(f"The Ascii code for {character} is {value}")
else:
    print("Too many characters")
print("Program Ended!")
