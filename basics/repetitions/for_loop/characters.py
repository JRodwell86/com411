#user to enter markings
def run():
    markings = input("What strange markings do you see?")
    #print the markings individually
    for position in range(0,len(markings),1):
        print(f"index {position}: ",end="")
        print(markings[position])
    print("Done!")




