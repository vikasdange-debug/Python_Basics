#CREATE STUDENT CLASS THAT TAKES NAME AND MARKS OF 3 SUBJECTS AS ARGUEMENTS IN INSTRUCTOR.
#THEN CREATE A METHOD TO PRINT THE AVERAGE

class Student :

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi!",self.name,"Your avg score is:",sum/3)

s1=Student("vikas",[98,90,85])
s1.get_avg()


