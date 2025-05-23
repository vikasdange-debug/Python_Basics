#PRINT SQUARE,SQUARE ROOT AND CUBE OF A NUMBER USING CLASS

class Calculator:
    def __init__(self,number):
        self.number=number

    def square(self):
        self.square=self.number*self.number
        return self.square

    def cube(self):
        self.cube=self.number*self.number*self.number
        return self.cube

    def square_root(self):
        self.square_root=self.number**0.5     
        return self.square_root
    
x=Calculator(25)                    
print( Calculator.square(x))       #Prints square of 25
y=Calculator(4)
print(Calculator.cube(y))        #Prints cube of 4
z=Calculator(11)
print(Calculator.square_root(z))        #Prints square root of 11