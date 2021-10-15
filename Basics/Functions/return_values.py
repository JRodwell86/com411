#function for beep weight
def beep_weight():
    print("How much does beep weigh?")
    beep = int(input())
    return beep
# function for bop weight
def bop_weight():
    print("How much does bop weigh?")
    bop = int(input())
    return bop
# function for average or sum
def sum_avg(Beep, Bop):
    print("What would you like to calculate (sum or average?)")
    answer = input()
    if answer == "sum":
        sum = Beep + Bop
        print(f"The sum of Beep and Bop's weight is {sum}")
    elif answer == "average":
        average = Beep + Bop / 2
        print(f"The average of Beep and Bop's weight is {average}")
    else:
        print("Wrong input")
# call to function
def run():
    beep = beep_weight()
    bop = bop_weight()
    sum_avg(beep, bop)

run()