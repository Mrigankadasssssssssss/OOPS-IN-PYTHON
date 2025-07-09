class Employee:
    def __init__(self):
        self.name = "Mriganka"
        self.id = 123
        self.designation = 'ML-Engineer'
        self.salary = 85000

    def travel(self,dest):
        print(f'Employee {self.name} is travelling to {dest}')

# creating a object
emp1 = Employee()

# print(emp1.name,',',emp1.designation,',',emp1.id
#       ,',',emp1.salary)

emp1.travel('Bangaluru')