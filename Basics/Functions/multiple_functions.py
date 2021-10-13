def display_ladder(steps):

    print(f"|   |\n" 
           "*****\n"
           "|   |\n" * steps)

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)


create_ladder()
