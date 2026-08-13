#Challenge 1: Student Management System

class Student:
    school_name = "ABC College"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_student(self):
        print("School Name :", Student.school_name)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)
        print("------------------------")

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


# Creating Objects
student1 = Student("Rahul", 20, "BCA")
student2 = Student("Priya", 19, "BSc")

print("Before Changing School Name")
student1.display_student()
student2.display_student()

Student.change_school_name("XYZ College")

print("After Changing School Name")
student1.display_student()
student2.display_student()


#Challenge 2: Employee Counter

class Employee:
    employee_count = 0

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee(self):
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Salary :", self.salary)
        print("------------------------")

    @classmethod
    def show_total_employees(cls):
        print("Total Employees :", cls.employee_count)


# Creating Objects
emp1 = Employee(101, "Amit", 50000)
emp2 = Employee(102, "Neha", 60000)
emp3 = Employee(103, "Raj", 55000)

emp1.display_employee()
emp2.display_employee()
emp3.display_employee()

Employee.show_total_employees()


#Challenge 3: Bank Account System

class BankAccount:
    bank_name = "State Bank of India"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Bank :", BankAccount.bank_name)
        print("Account Number :", self.account_number)
        print("Holder Name :", self.holder_name)
        print("Current Balance : ₹", self.balance)
        print("------------------------")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


# Creating Objects
acc1 = BankAccount(1001, "Rahul", 10000)
acc2 = BankAccount(1002, "Priya", 15000)

acc1.deposit(5000)
acc1.withdraw(3000)
acc1.check_balance()

acc2.deposit(2000)
acc2.withdraw(500)
acc2.check_balance()

BankAccount.change_bank_name("Punjab National Bank")

print("After Changing Bank Name")
acc1.check_balance()
acc2.check_balance()


#Challenge 4: Mobile Store Inventory

class Mobile:
    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_mobile(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price : ₹", self.price)

    def calculate_discount_price(self):
        discount = self.price * Mobile.discount_percentage / 100
        final_price = self.price - discount
        print("Discounted Price : ₹", final_price)
        print("------------------------")

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount


# Creating Objects
m1 = Mobile("Samsung", "Galaxy S24", 70000)
m2 = Mobile("Apple", "iPhone 15", 80000)
m3 = Mobile("OnePlus", "12R", 45000)

print("Before Discount Change")
m1.display_mobile()
m1.calculate_discount_price()

m2.display_mobile()
m2.calculate_discount_price()

m3.display_mobile()
m3.calculate_discount_price()

Mobile.change_discount(20)

print("After Discount Change")

m1.calculate_discount_price()
m2.calculate_discount_price()
m3.calculate_discount_price()


#Challenge 5: Library Book Management

class Book:
    library_name = "City Library"

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book_info(self):
        print("Library :", Book.library_name)
        print("Book ID :", self.book_id)
        print("Title :", self.title)
        print("Author :", self.author)
        print("------------------------")

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name


# Creating Objects
book1 = Book(1, "Python Programming", "Guido van Rossum")
book2 = Book(2, "Data Structures", "Mark Allen")
book3 = Book(3, "Machine Learning", "Tom Mitchell")

print("Before Changing Library Name")

book1.display_book_info()
book2.display_book_info()
book3.display_book_info()

Book.change_library_name("National Digital Library")

print("After Changing Library Name")

book1.display_book_info()
book2.display_book_info()
book3.display_book_info()
