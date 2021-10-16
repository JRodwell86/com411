#input rows and columns
def run():
    rows = int(input("How many rows should I have?"))
    columns = int(input("How many columns should I have?"))
    #print smiley
    for row in range(0,rows,1):
        for column in range(0,columns,1):
            print(":-)", end="")
        print("")


