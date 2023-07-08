class Circle:
    pi=3.14

    def __init__(self,radius):
        self.radius = radius

    def reset(self,newradius):
        self.newradius = newradius
        self.area = 2*newradius*newradius*Circle.pi

a= Circle()
print(a.radius)
a.reset()