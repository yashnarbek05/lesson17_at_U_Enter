class Employee:
    def __init__(self,name=None,age=None,salary=None,gender=None):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of employee is", self.name)
        print("age of employee is", self.age)
        print("salary of employee is", self.salary)
        print("gender of employee is", self.gender)

    def __str__(self):
        return f"str: {self.name} {self.age} {self.gender} {self.salary}"

    def __repr__(self):
        return f"repr: {self.name} {self.age} {self.gender} {self.salary}"