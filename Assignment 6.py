#SECTION 1: HYBRID INHERITANCE

#Question 1: School Management System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll):
        Person.__init__(self, name, age)
        self.roll = roll

class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll, subject):
        Student.__init__(self, name, age, roll)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll)
        print("Subject:", self.subject)

ta = TeachingAssistant("raj", 22, 101, "Python")
ta.display()

#Question 2: Vehicle Management System

class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class ElectricCar(Car):
    def battery(self):
        print("Battery Powered")

class SportsElectricCar(ElectricCar):
    def speed(self):
        print("High Speed")

car = SportsElectricCar()
car.start()
car.battery()
car.speed()

#Question 3: Employee System

class Employee:
    def work(self):
        print("Employee Working")

class Developer(Employee):
    def coding(self):
        print("Writing Code")

class Manager(Employee):
    def manage(self):
        print("Managing Team")

class TechLead(Developer, Manager):
    def display(self):
        self.coding()
        self.manage()

t = TechLead()
t.display()

#Question 4: Hospital System

class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def treat(self):
        print(self.name, "Treats Patients")

class Nurse(Person):
    def assist(self):
        print(self.name, "Assists Doctor")

class HeadNurse(Nurse):
    def supervise(self):
        print(self.name, "Supervises Nurses")

h = HeadNurse("Priya")
h.assist()
h.supervise()


#SECTION 2: HIERARCHICAL INHERITANCE

#Question 5: Animal Class

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

class Cow(Animal):
    def sound(self):
        print("Cow Moos")

Dog().sound()
Cat().sound()
Cow().sound()

#Question 6: Bank Account

class BankAccount:
    def info(self):
        print("Bank Account")

class SavingsAccount(BankAccount):
    def info(self):
        print("Savings Account")

class CurrentAccount(BankAccount):
    def info(self):
        print("Current Account")

class FixedDepositAccount(BankAccount):
    def info(self):
        print("Fixed Deposit Account")

SavingsAccount().info()
CurrentAccount().info()
FixedDepositAccount().info()

#Question 7: Employee

class Employee:
    def work(self):
        print("Employee Works")

class Developer(Employee):
    def work(self):
        print("Developer Writes Code")

class Tester(Employee):
    def work(self):
        print("Tester Tests Software")

class Designer(Employee):
    def work(self):
        print("Designer Creates UI")

Developer().work()
Tester().work()
Designer().work()

#Question 8: Shape Area

class Shape:
    pass

class Circle(Shape):
    def area(self, r):
        print("Area =", 3.14 * r * r)

class Rectangle(Shape):
    def area(self, l, b):
        print("Area =", l * b)

class Square(Shape):
    def area(self, s):
        print("Area =", s * s)

Circle().area(5)
Rectangle().area(4, 6)
Square().area(5)


#SECTION 3: POLYMORPHISM

#Question 9: Shape Area

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area")

class Triangle(Shape):
    def area(self):
        print("Triangle Area")

shapes = [Circle(), Rectangle(), Triangle()]

for s in shapes:
    s.area()

#Question 10: Payment

class Payment:
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")

class NetBankingPayment(Payment):
    def pay(self):
        print("Paid using Net Banking")

payments = [CreditCardPayment(), UPIPayment(), NetBankingPayment()]

for p in payments:
    p.pay()

#Question 11: Notification

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email Sent")

class SMSNotification(Notification):
    def send(self):
        print("SMS Sent")

class PushNotification(Notification):
    def send(self):
        print("Push Notification Sent")

notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for n in notifications:
    n.send()

#Question 12: Animal Sounds

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Lion(Animal):
    def make_sound(self):
        print("Roar")

animals = [Dog(), Cat(), Lion()]

for a in animals:
    a.make_sound()

#Question 13: Employee Roles

class Employee:
    def role(self):
        pass

class Developer(Employee):
    def role(self):
        print("Developer")

class Tester(Employee):
    def role(self):
        print("Tester")

class Manager(Employee):
    def role(self):
        print("Manager")

employees = [Developer(), Tester(), Manager()]

for e in employees:
    e.role()

#Question 14: Vehicle Start

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

class Bus(Vehicle):
    def start(self):
        print("Bus Started")

vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()



#SECTION 4: POLYMORPHISM + INHERITANCE

#Question 15: Device System

class Device:
    def operate(self):
        print("Device Operating")

class Camera(Device):
    def operate(self):
        print("Camera Capturing Photos")

class Phone(Device):
    def operate(self):
        print("Phone Making Calls")

class SmartPhone(Phone):
    def operate(self):
        print("SmartPhone Calling and Taking Photos")

devices = [Camera(), Phone(), SmartPhone()]

for d in devices:
    d.operate()