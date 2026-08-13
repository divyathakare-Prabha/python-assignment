#Question 1: Student Class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Amit", 20)
s2 = Student("Priya", 21)
s3 = Student("Rahul", 19)

s1.display()
s2.display()
s3.display()

#Question 2: Employee Class

class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display(self):
        print(self.employee_id, self.employee_name, self.salary)

e1 = Employee(101, "John", 50000)
e1.display()

#Question 3: Car Class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

c1 = Car("Toyota", "Innova")
c1.display()

#Question 4: BankAccount Class

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)

#Question 5: Book Class

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title, "-", self.author)

b1 = Book("Python", "ABC")
b2 = Book("Java", "XYZ")

b1.display()
b2.display()

#Question 6: Mobile Class

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m = Mobile("Samsung", 25000)
m.display()

#Question 7: Company Class

class Company:
    company_name = "Infosys"

    def __init__(self, employee):
        self.employee = employee

    def display(self):
        print(self.employee, Company.company_name)

e1 = Company("Amit")
e2 = Company("Priya")

e1.display()
e2.display()

#Question 8: Product Class

class Product:
    tax_rate = 18

    def __init__(self, price):
        self.price = price

    def final_price(self):
        total = self.price + (self.price * Product.tax_rate / 100)
        print("Final Price:", total)

p = Product(1000)
p.final_price()

#Question 9: Student Class Method

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_school(cls, new_name):
        cls.school = new_name

    def display(self):
        print(self.name, Student.school)

s1 = Student("Amit")
s1.display()

Student.update_school("XYZ School")
s1.display()

#Question 10: Vehicle Count

class Vehicle:
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

v1 = Vehicle()
v2 = Vehicle()
v3 = Vehicle()

print("Total Vehicles:", Vehicle.vehicle_count)

#Question 11: Calculator

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

print(Calculator.add(10, 5))
print(Calculator.subtract(10, 5))
print(Calculator.multiply(10, 5))
print(Calculator.divide(10, 5))

#Question 12: Temperature Converter

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))

#Question 13: Utility Class

class Utility:

    @staticmethod
    def even_odd(n):
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")

Utility.even_odd(8)

#Question 14: Person and Student

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print(self.name, self.roll)

s = Student("Amit", 101)
s.display()

#Question 15: Vehicle and Bike

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print(self.brand, self.model)

b = Bike("Honda", "Shine")
b.display()

#Question 16: Shape

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self, r):
        print(3.14 * r * r)

class Rectangle(Shape):
    def area(self, l, b):
        print(l * b)

c = Circle()
c.area(5)

r = Rectangle()
r.area(4, 6)

#Question 17: Animal

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()

#Question 18: Private Salary

class Person:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

p = Person()

print(p.get_salary())

p.set_salary(70000)

print(p.get_salary())

#Question 19: Bank Account Encapsulation

class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

a = BankAccount()

a.deposit(500)

print(a.get_balance())

#Question 20: Employee Private Data

class Employee:
    def __init__(self):
        self.__salary = 30000

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee()

e.set_salary(45000)

print(e.get_salary())

#Question 21: Library Management System


class Library:
    def __init__(self, book):
        self.book = book

    def issue(self):
        print(self.book, "Issued")

    def return_book(self):
        print(self.book, "Returned")

l = Library("Python")

l.issue()
l.return_book()

#Question 22: Hospital Management System

class Hospital:
    def __init__(self):
        self.__hospital = "City Hospital"

    def get_hospital(self):
        return self.__hospital

class Patient(Hospital):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def display(self):
        print(self.name, self.get_hospital())

p = Patient("Rahul")
p.display()

#Question 23: School Management System

class School:
    school_name = "ABC School"

    def __init__(self, student):
        self.student = student

    @classmethod
    def change_school(cls, name):
        cls.school_name = name

    def display(self):
        print(self.student, School.school_name)

s = School("Amit")

s.display()

School.change_school("XYZ School")

s.display()

#Question 24: Online Shopping System

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def display(self):
        print(self.name, self.price)

e = Electronics("Laptop", 60000)

e.display()

#Question 25: Mini ATM System

class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Balance:", self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Balance:", self.__balance)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.__balance)

atm = ATM(5000)

atm.deposit(1000)
atm.withdraw(2000)
atm.check_balance()