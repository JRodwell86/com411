def create_ladder():
    print("How many steps remain?")
    rung = int(input())
    return rung

def draw_ladder():
    for step in range(steps):
        print("|    |")
        print(" ****")
    print("|    |")


steps = int(create_ladder())
draw_ladder()