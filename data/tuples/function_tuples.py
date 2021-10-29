#function to create a tuple & return it directly
def likelihood():
    return (50, 38, 27, 99, 4)

#function to call previous function
def run():
    # code to show minimum and max from tuple
    print(f"Minimum likelihood of falling: {min(likelihood())}%")
    print(f"Minimum likelihood of falling: {max(likelihood())}%")

if __name__ == "__main__":
    run()