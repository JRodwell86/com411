print("Program Started...")
print()
# input ascii code & confirm positive number
character = abs(int(input("Please enter an ascii code")))
print()
# convert to ascii
ascii_character = chr(character)
# print outcome if within range
if abs(character) in range(32, 126, 1):
    print(f"The character represented by the ascii code {character} is {ascii_character}")
else:
    print(f"This code is not in range 32-126")
print()
print("Program Ended!")

#print("Program Started!")

#print("Please enter an ASCII code:")
#code = int(input())

#if code >= 32 and code <= 126:
 #   print(f"The character represented by the ASCII value {code} is: {chr(code)}")
#else:
 #   print("The character cannot be displayed.")

#print("Program Ended!")