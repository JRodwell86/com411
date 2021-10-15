#ask user to enter meal choices
main = input("What would you like for your main?")
side = input("What would you like for your side?")
drink = input("What would you like to drink?")
happy = int(input("How happy are you with your dinner? (Scale of 1-10)"))

print(f"You would like to eat {main} with a side of {side}. You would like to drink {drink}")
print(f"You are this happy with your dinner: {'♥' * happy}")
