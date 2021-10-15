#user to choose a kind of film
genre = input("Please enter a genre of film (Sci Fi/Rom Com)")
if genre == "sci fi":
    type1 = input("do you want to watch a robot film?(yes/no)")
    type2 = input("do you want to watch an alien film?(yes/no)")
    if (type1 == "yes") and (type2 =="yes"):
        print("You should watch Beep from space")
    else:
        print("you should watch swamp guy from earth")
elif genre == "rom com":
    type1 = input("do you want to watch a wedding film?(yes/no)")
    type2 = input("do you want to watch an christmas film?(yes/no)")
    if (type1 == "yes") and (type2 =="yes"):
        print("You should watch Beep get married in lapland")
    else:
        print("you should watch Kiss Kiss the movie")
else:
    print("Maybe you should go to bed")