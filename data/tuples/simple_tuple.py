#function to create a tuple & return
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods
#function to call previous function and populate value
def run():
    value = likelihood()
# code to show minimum from tuple
    print(f"Minimum likelihood of falling: {min(value)}%")

if __name__ == "__main__":
    run()