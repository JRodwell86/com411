class Human:
    MAX_ENERGY = 100

    def __init__(self, name= "Human", age = 0, energy = MAX_ENERGY):
        #initial state of a person - the default of the person

        self.name = name
        self.age = 0
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")
        print(self.energy)


if (__name__ == "__main__"):
  human = Human()
  human.display()