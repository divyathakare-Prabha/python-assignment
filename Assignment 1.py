#Section 1
#Q1. Display name, college name, and favorite programming language

print("Name: Sham")
print("College: Zeal College")
print("Favorite Programming Language: Python")


#Q2. Take user input for name and age

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")


#Q3. Create variables and print them

student_name = "Sham"
roll_number = 25
percentage = 89.5
passed = True

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Percentage:", percentage)
print("Passed:", passed)


#Q4. Invalid variable names

#Invalid       	Correct
#1name	        name1
#student-name	student_name
#class       	class_name
#total marks	    total_marks
#user_name	    Valid


#Section 2

#Q5. Data types

a = 10
b = 15.5
c = "Python"
d = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


#Q6. Sum of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)


#Q7. Type conversion

num = float(input("Enter decimal number: "))

print("Integer:", int(num))
print("String:", str(num))


#Q8. Check input type

age = input("Enter age: ")
print(type(age))

age = int(age)

print(type(age))


#Section 3
#Q9. Arithmetic operations

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)


#Q10. Comparison operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a > b)
print(a < b)
print(a == b)
print(a != b)


#Q11. Login system

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")


#Q12. Positive, Negative or Zero

num = float(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#Section 4

#Q13. Grade

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


#Q14. Even or Odd

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#Q15. Age category

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")


#Q16. Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
else:
    print("Invalid Choice")


#Section 5

#Q17. Numbers 1 to 20

for i in range(1, 21):
    print(i)


#Q18. Even numbers

for i in range(2, 51, 2):
    print(i)


#Q19. Multiplication table

num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#Q20. While loop 10 to 1

i = 10

while i >= 1:
    print(i)
    i -= 1


#Q21. Sum 1 to 100

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)


#Q22. Count digits

num = input("Enter number: ")

print("Digits =", len(num))


#Section 6

#Q23. Break

for i in range(1, 21):
    if i == 15:
        break
    print(i)


#Q24. Continue

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


#Q25. Password check

while True:
    password = input("Enter password: ")

    if password == "1234":
        print("Correct Password")
        break
    else:
        print("Wrong Password")
#Section 7

#Q26. Pattern

for i in range(1, 6):
    print("*" * i)


#Q27. Multiplication table 1 to 5

for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()


#Q28. Number square

for i in range(1, 5):
    print(str(i) * 4)


#Section 8

#Q29. Student list

students = ["Amit", "Sham", "Riya", "Neha", "Rahul"]

print("First:", students[0])
print("Last:", students[-1])
print("Total:", len(students))


#Q30. Store 5 numbers

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print(numbers)


#Q31. List operations

numbers = [5, 3, 8]

numbers.append(10)
numbers.remove(3)
numbers.pop()
numbers.sort()

print(numbers)


#Q32. Print list using loop

numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i)


#Q33. Max, Min, Sum

numbers = [10, 5, 20, 30, 15]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


#Q34. List slicing

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[:5])
print(numbers[-3:])
print(numbers[::2])


#Section 9

#Q35. Tuple

student = ("Sham", 22, "Pune")

print(student[0])
print(student[1])
print(student[2])

#Q36. Change tuple value

student = ("Sham", 22, "Pune")

student[0] = "Ram"

#Output:

#TypeError: 'tuple' object does not support item assignment


#Q37. Tuple operations

numbers = (10, 5, 20, 40, 15)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


#Q38. Tuple packing and unpacking

student = ("Sham", 22, "Pune")

name, age, city = student

print(name)
print(age)
print(city)

#Section 10

#Q39. Mini ATM

balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        balance += amount
        print("Amount Deposited")

    elif choice == 3:
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")

#Q40. Student Result Management

marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Marks:", marks)
print("Average:", average)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
print("Highest Marks:", max(marks))