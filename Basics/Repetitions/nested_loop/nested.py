rows = int(input("How many rows should I have?"))
columns = int(input("How many columns should I have?"))
row_number = 0
column_number = 0
for column_number in range(columns):
    print(f":-)" * column_number, end="")
    for row_number in range(rows):
        print(f":-)")


