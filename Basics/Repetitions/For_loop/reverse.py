phrase = input("What phrase do you see?")
print(phrase)
print("\nReversing...")
print("\nThe Phrase is:", end="")
for position in range(len(phrase)-1,-1,-1):
     print(phrase[position], end="")