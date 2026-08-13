#QUESTION 1: ABSTRACT CLASS & ABSTRACT METHOD

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car is starting...")

c = Car()
c.start()


#Output

#Car is starting...

#QUESTION 2: ABSTRACT CLASS WITH MULTIPLE CHILD CLASSES

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
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

#Output

#Dog barks
#Cat meows

#QUESTION 3: POLYMORPHISM USING METHOD OVERRIDING

class Shape:

    def draw(self):
        print("Drawing Shape")

class Circle(Shape):

    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):

    def draw(self):
        print("Drawing Rectangle")

c = Circle()
r = Rectangle()

c.draw()
r.draw()

#Output

#Drawing Circle
#Drawing Rectangle

#QUESTION 4: POLYMORPHISM WITH LOOP

class Bird:

    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):

    def fly(self):
        print("Sparrow flies low")

class Eagle(Bird):

    def fly(self):
        print("Eagle flies high")

birds = [Sparrow(), Eagle()]

for bird in birds:
    bird.fly()

#Output

#Sparrow flies low
#Eagle flies high

#QUESTION 5: ABSTRACT CLASS + POLYMORPHISM

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Developer writes code")

class Designer(Employee):

    def work(self):
        print("Designer creates UI")

employees = [Developer(), Designer()]

for emp in employees:
    emp.work()

#Output


#Developer writes code
#Designer creates UI