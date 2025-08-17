


class Student:
    def __init__(self,name,grade):
      self.name = name
      self.grade = grade
    def __str__(self):
        return f"{self.name}({self.grade})"
    def myfun(self):
        print("Hello my name is "+self.name+" my grade is "+self.grade)
p1 = Student("ramees","A+")
print(p1.name)
print(p1.grade)
print(p1)
p1.myfun()
