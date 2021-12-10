class Robot:
    MAX_ENERGY = 100

    def __init__(self, name= "Robot", age = 0):
        #initial state of a person - the default of the person

        self.name = name
        self.age = 0
        self.energy = Robot.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")
        print(self.energy)


if (__name__ == "__main__"):
  robot = Robot()
  robot.display()