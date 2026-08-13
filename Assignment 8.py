#Question 1: Abstract Class & Abstract Method

from abc import ABC, abstractmethod

# Abstract Class

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

# Child Class

class Car(Vehicle):

    def start(self):
        print("Car is starting...")

# Object Creation

c = Car()
c.start()

#Output

#Car is starting...

#Question 2: Abstract Class with Multiple Child Classes

from abc import ABC, abstractmethod

# Abstract Class

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child Class

class Dog(Animal):

    def sound(self):
        print("Dog barks")

# Child Class

class Cat(Animal):

    def sound(self):
        print("Cat meows")

# Objects

d = Dog()
c = Cat()

d.sound()
c.sound()

#Output

#Dog barks
#Cat meows

#Question 3: Polymorphism Using Method Overriding

# Parent Class

class Shape:

    def draw(self):
        print("Drawing Shape")

# Child Class

class Circle(Shape):

    def draw(self):
        print("Drawing Circle")

# Child Class

class Rectangle(Shape):

    def draw(self):
        print("Drawing Rectangle")

# Objects

c = Circle()
r = Rectangle()

c.draw()
r.draw()

#Output

#Drawing Circle
#Drawing Rectangle

#Question 4: Polymorphism with Loop

# Parent Class

class Bird:

    def fly(self):
        print("Bird flies")

# Child Class

class Sparrow(Bird):

    def fly(self):
        print("Sparrow flies low")

# Child Class

class Eagle(Bird):

    def fly(self):
        print("Eagle flies high")

# List of Objects

birds = [Sparrow(), Eagle()]

# Loop

for bird in birds:
    bird.fly()

#Output

#Sparrow flies low
#Eagle flies high

#Question 5: Abstract Class + Polymorphism

from abc import ABC, abstractmethod

# Abstract Class

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

# Child Class

class Developer(Employee):

    def work(self):
        print("Developer writes code")

# Child Class

class Designer(Employee):

    def work(self):
        print("Designer creates UI designs")

# List of Objects

employees = [Developer(), Designer()]

# Loop

for emp in employees:
    emp.work()

#Output

#Developer writes code
#Designer creates UI designs

