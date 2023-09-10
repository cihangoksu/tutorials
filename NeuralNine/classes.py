from unicodedata import name
from urllib.parse import _NetlocResultMixinBytes


class Person:
    amount = 0
    def __init__(self, name, age, height):
        print(f'Hello {name}, you are  {age} years old')
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    

    def get_older(self, years):
        self.age += years


    def __str__(self):
        return f"Person {self.name} is {self.age} years old and {self.height} cm."

    def __del__(self):
        print('Person object is deleted')
        Person.amount -= 1




class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        new_text = super(Worker,self).__str__() + f'His/her salary is {self.salary} Euros'
        return new_text


    def calc_annual_salary(self):
        return self.salary + 12




class Boss(Worker):
    def __init__(self, name, age, height, salary, count_employees):
        super(Boss, self).__init__(name, age, height, salary)
        self.count_employees = count_employees

    def __str__(self):
        new_text = super(Boss, self).__str__() + f'He has {self.count_employees} employees'
        return new_text


Boss1 = Boss('Cihan', 40, 177, 3000, 25)
print(Boss1)