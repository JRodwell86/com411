

def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
#variable to bring the list from the function above
    path = movements()
    print(f"{path[0]} for {path[1]}")
    print(f"{path[2]} for {path[3]}")
    print(f"{path[4]} for {path[5]}")
    print(f"{path[6]} for {path[7]}")

if __name__ == "__main__":
    run()