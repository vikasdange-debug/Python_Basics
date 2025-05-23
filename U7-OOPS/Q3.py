#DEFINE A EMPLOYEE CLASS WITH ATTRIBUTES,ROLE AND SALARY.THIS CLASS CONTAINS SHOW DETAILS METHOD
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def show_details(self):
        print ("role=",self.role)
        print ("Department=",self.dept)
        print ("Salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")
               
Engg1=Engineer("vikas dange","20")
print(Engg1.show_details())

#CREATE AN ENGINEER CLASS THAT INHERITS PROPERTIES FROM EMPLOYEE AND HAS ADDITIONAL ATTRIBUTES,,NAME AND AGE