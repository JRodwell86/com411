bars = 0
amount = int(input("How many many bars should be charged?"))
while bars < amount:
    bars = bars + 1
    print(f"Charging: {bars}")
    print(f" {bars}", end="")
print("The battery is fully charged")