class Student:
 
    def __init__(self,name,age,gender):
        
        self.name   = name
        self.age    = age
        self.gender = gender

    def printer(self):
        
        print(f"the age of {self.name} is {self.age}")
    
class Teacher(Student):
    
    def __init__(self,name,age,gender,tsc_no,hours_worked):
        """uper is a function that returns a proxy object that delegates method calls to a parent
           or sibling class"""

        super().__init__(name,age,gender)
        self.tsc_no       = tsc_no
        self.hours_worked = hours_worked
             
    def who_am_i(self):
        
        print("I am a Teacher")

    def set_college(self):
        
        self.college = input("Enter the college you attended: ")
    
        return self.college
    
    def get_salary(self):

        return self.hours_worked * 2000    

mwalimu = Teacher("kamau", 23, "male", 12345, 8)        
