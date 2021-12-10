class Person:
    # attributes
    #name, age, weight - this is how we're going to define a person and what their attributes are
    # =0 sets optional defaults values of 0
    def __init__(self, name, age=0, weight=0):
        #initial state of a person - the default of the person
        self.name = name
        self.age = age
        self.weight = weight


    #behaviours
    #display_info
# method to change the name of a person - calls 'self' - specific instance and new_name - parameter of name
def change_name(self, new_name):
    #code to change the name
    self.name = new_name

def display(self):
    print(f"{self.name} is {self.age} years old and weighs {self.weight}kg")

jane = Person("Jane Smith", 30, 87)

display(jane)
change_name(jane, "Bert")
display(jane)
