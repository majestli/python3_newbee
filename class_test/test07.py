import  math
class Shape:
    def area(self):
        return 0.0
class Circle(Shape):
    def __init__(self,r=0.0):
        self.r=r
    def area(self):
        return math.pi*self.r*self.r
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a,self.b= a,b
    def area(self):
        return self.a*self.b



circle=Circle(3.0)
print(circle.area())


rectangle= Rectangle(2.0,3.0)
print(rectangle.area())


print(Shape.__dict__['area'])
print(Circle.__dict__['area'])
