class Employee:
    def __init__(self,name,emp_no,department):
        self.name = name
        self.emp_no = emp_no
        self.department = department
        self.salary = salary
    def display_info(self):
        return f"Employee: {self.name},Department: {self.department} Employee code : {self.emp_no}"
class Manager(Employee):
    def __init__(self, name, emp_no,department,salary,):
        super().__init__(name,emp_no,department)
        self.salary = salary
    def display_info(self):
        return f"Employee: {self.name},Department: {self.department} Employee code : {self.emp_no} salary is {self.salary}"

emp1 =     


