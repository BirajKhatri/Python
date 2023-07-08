class Animal:
    def __init__(self):
        print("Animal class created")
    
    def whols(self):
        print("Animal")
    
    def eat(self):
        print("Animal who eat meat")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog class created')
    def whois(self):
        print('Animal type is dog')

a= Animal()
b=Dog()
b.whois()
b.eat()