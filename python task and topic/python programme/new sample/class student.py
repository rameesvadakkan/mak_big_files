class Student :
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def student_details(self):
        print(f"student name {self.name} and Grade:{self.grade}")

s = Student("ramees",'A')
s.student_details()


            