cables = 0
amount = int(input("How many live cables are there?"))
while cables < amount:
    cables = cables + 1
    print("avoiding...", end="")
    print(f"...Done! Avoided {cables} live cables ")
print("All live cables have been avoided")