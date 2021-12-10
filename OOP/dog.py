# first create the class with a capital letter
class Dog:
# creates the attributes of the class - self is always there but can always pass in parameters as seen below)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # parameter integer - can be used for maths e.g adding energy
        self.energy = 50
        # parameter boolean - can change state - eg bad dog
        self.is_good_dog = True
        self.is_indoors = True
# method - can be used to change variable
# so this one subtracts to the energy - called run because the dog is 'running'
    def run(self):
        self.energy -= 5
# this one adds to energy cos eats
    def eat(self):
        self.energy += 5
# this one includes an if statement that if the dof is inside then good dog is changed to fales
    def go_to_toilet(self):
        if self.is_indoors:
            self.is_good_dog = False
            # seperate from if statement about energy is added.
        self.energy += 5
# code to create two separate dogs, with parameters
first_dog = Dog("Fido", "Pert")
second_dog = Dog("Derp", "Slurp")

# run the functions to work through the above
first_dog.eat()
second_dog.run()
second_dog.go_to_toilet()


# prints the name and surname of the first dog
print(first_dog.name, first_dog.surname)
# prints energy of the first dog after it eats - so is +5
print(first_dog.energy)
# second dog pooped inside so good dog is now false.
print(second_dog.is_good_dog)





