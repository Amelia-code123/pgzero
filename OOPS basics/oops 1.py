#defining a class
class person():
    #common properties
    city="Chelmsford"
    age=30
    #constructor
    def __init__(self):
        print("Object is created")
    #functions
    def details(self):
        self.name=input("what is your name?")
        self.year=input("what year are you in?")
        self.colour=input("what is your favourite colour?")
    def display(self):
        print(self.name)
        print(self.year)
        print(self.colour)

#object creation
p1=person()
print(p1.city)
print(p1.age)
p1.details()
p1.display()

p2=person()
print(p2.city)
print(p2.age)
p2.details()
p2.display()