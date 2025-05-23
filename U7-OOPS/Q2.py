#DEFINE A CIRCLE CLASS TO CREATE A CIRCLE WITH RADIUS R USING A CONSTRUCTOR
#DEFINE AN AREA() METHOD OF THE CLASS WHICH CALCULATES THE AREA OF CIRCLE
#DEFINE A PERIMETER() METHOD OF THE CLASS WHICH ALLOWS YOU TO CALCULATE THE PERIMETER OF CIRCLE

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius*self.radius


    def perimeter(self):
        return 2*(22/7)*self.radius
       

    
parameters=Circle(21)
print(parameters.area())
print(parameters.perimeter())