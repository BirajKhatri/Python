# it is a state of object
# the syntax for creating an attributes is

# self.attributes=something

# init is special method which is called
# automatically right after an object has been created

class Fruit:
    def __init__(self,name):
        self.name=name

x= Fruit(name='Apple')
print(x.name)