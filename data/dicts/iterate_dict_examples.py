wedding = {"Cake":1, "Car":1, "Ribbons":100}
for key in wedding.keys():
    print(key)

for value in wedding.values():
    print(value)

for key, value in wedding.items():
    print(f"{key}: {value}")