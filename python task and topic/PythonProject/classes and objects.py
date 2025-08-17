class Person:
    def __init__(self,name,standard):
        self.name = name
        self.standard = standard
    def displaydetails(self):
        print(f"Student name is {self.name} and studying in {self.standard}")
class Student(Person):
    def __init__(self,name,standard,lname):
        self.lname = lname
        super().__init__(name,standard)
    def lastname(self):
        print(f"Fullname is {self.name}{self.lname}")

details = Person("Ruhaan",1)
details1 = Person("Asna",10)
details2 = Person("Ramees",12)
fullname = Student("ramees ",12,"vadakkan")
'''
details.displaydetails()
details1.displaydetails()
details2.displaydetails()
fullname.lastname()'''
fullname.displaydetails()
fullname.lastname()


