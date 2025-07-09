# Create class 'Programmer' storing info of programers

class Programmer:
    
    def __init__(self):
        empid = int(input("What is the employee id?\n"))
        name = input("What is the name of the employee?\n")
        salary = int(input("What is the Salary?\n"))
        self.empid = empid
        self.name = name
        self.salary = salary
    
    def print_details(self):
        print(f'''The name is {self.name}
employee id is {self.empid}
salary is {self.salary}''')
    
    @staticmethod
    def greet():
        print("Ohayo onichan...")

baka = Programmer()
baka.greet()
baka.print_details()