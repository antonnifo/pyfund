class Student:
    def __init__(self, student_id, student_name, class_, gpa):
        self.std_id = int(student_id)
        self.std_name = str(student_name)
        self.class_ = int(class_)
        self.gpa = float(gpa)
    
    def print_std_details(self):
        print(f"{self.std_id} {self.std_name} {self.class_} {self.gpa}")

std_1 = Student(10015, 'Smith, John', 4, 3.01)
std_2 = Student(10167, 'Jones, Wendy', 1, 2.85)
std_3 = Student(10175, 'Smith, Jane', 4, 3.92)
std_4 = Student(10188, 'Wales, Sam', 4, 3.25)
std_5 = Student(10200, 'Robert, Sally', 4, 4.00)
std_6 = Student(10208, 'Green, Patrick', 1, 3.85)
std_7 = Student(10226, 'Nelson, Amy', 3, 2.95)
std_8 = Student(10334, 'Roberts, Jane', 3, 3.81)
std_9 = Student(10387, 'Taylor, Susan', 3, 3.33)
std_10 = Student(10400, 'Logan, Mark', 1, 3.3)
std_11 = Student(10485, 'Brown, Jessica', 3, 2.91)

student_objects = [std_1,std_2,std_3,std_4,std_5,std_6,std_7,std_8,std_9,std_10,std_11]

for student in student_objects:
    student.print_std_details()
