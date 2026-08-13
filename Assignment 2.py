#Section 1: Dictionary Challenges

#Q1. Create a dictionary to store Student name, Age, Course, City. Print all dictionary values.

student = {
    "name": "Sham",
    "age": 22,
    "course": "Python",
    "city": "Pune"
}

print("Student Details:")
for value in student.values():
    print(value)


#Q2. Create a dictionary of employee details and access Employee name, Salary, Department using keys.

employee = {
    "name": "Rahul",
    "salary": 50000,
    "department": "IT"
}

print("Employee Name:", employee["name"])
print("Salary:", employee["salary"])
print("Department:", employee["department"])

#Q3. Add a new key-value pair to an existing dictionary (Add "email").

student = {
    "name": "Sham",
    "age": 22,
    "course": "Python"
}

student["email"] = "sham@gmail.com"

print(student)

#Q4. Update the value of an existing key in a dictionary.

student = {
    "name": "Sham",
    "city": "Mumbai"
}

student["city"] = "Pune"

print(student)

#Q5. Remove a key using pop() and del.
student = {
    "name": "Sham",
    "age": 22,
    "city": "Pune"
}

student.pop("age")
print(student)

del student["city"]
print(student)

#Q6. Print all Keys, Values and Key-Value pairs using loops.

student = {
    "name": "Sham",
    "age": 22,
    "city": "Pune"
}

print("Keys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

#Q7. Count how many subjects are present in a student marks dictionary.

marks = {
    "Math": 90,
    "Science": 85,
    "English": 88,
    "History": 75
}

print("Total Subjects:", len(marks))

#Q8. Create a dictionary containing marks of 5 subjects and calculate total marks.

marks = {
    "Math": 90,
    "Science": 85,
    "English": 88,
    "History": 75,
    "Computer": 95
}

total = sum(marks.values())

print("Total Marks:", total)

#Q9. Check whether a key exists in a dictionary or not.

student = {
    "name": "Sham",
    "age": 22
}

key = input("Enter key to search: ")

if key in student:
    print("Key exists.")
else:
    print("Key not found.")


#Q10. Display products having price greater than 500.

products = {
    "Keyboard": 700,
    "Mouse": 400,
    "Monitor": 8000,
    "Pen": 20,
    "Headphones": 1200
}

print("Products above ₹500:")

for product, price in products.items():
    if price > 500:
        print(product, ":", price)


#Section 2: Set Challenges

#Q11. Create a set containing 5 numbers and print all elements.

numbers = {10, 20, 30, 40, 50}

for num in numbers:
    print(num)

#Q12. Add new elements using add().

numbers = {10, 20, 30}

numbers.add(40)
numbers.add(50)

print(numbers)

#Q13. Remove an element using remove() and discard().
numbers = {10, 20, 30, 40}

numbers.remove(20)
numbers.discard(30)

print(numbers)

#Q14. Perform Union, Intersection and Difference.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

#Q15. Find common elements between two sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Common Elements:", set1.intersection(set2))

#Q16. Check whether a value exists in a set.
numbers = {5, 10, 15, 20}

value = int(input("Enter value: "))

if value in numbers:
    print("Value Found")
else:
    print("Value Not Found")

#Q17. Convert a list with duplicate values into a set.
numbers = [10, 20, 20, 30, 40, 40, 50]

unique = set(numbers)

print(unique)

#Q18. Display total unique student names.
students = {"Rahul", "Sham", "Amit", "Rahul", "Neha"}

print("Unique Students:", len(students))

#Q19. Check whether two sets are equal.
set1 = {1, 2, 3}
set2 = {3, 2, 1}

if set1 == set2:
    print("Sets are Equal")
else:
    print("Sets are Not Equal")

#Q20. Remove all elements using clear().
numbers = {10, 20, 30, 40}

numbers.clear()

print(numbers)


#Section 3: Function Challenges
#Q21. Print "Welcome to Python Programming".

def welcome():
    print("Welcome to Python Programming")

welcome()

#Q22. Add two numbers.
def add(a, b):
    print("Sum =", a + b)

add(10, 20)

#Q23. Accept a name as parameter.
def greet(name):
    print("Hello,", name)

greet("Rohit")

#Q24. Find square of a number.
def square(num):
    print("Square =", num * num)

square(5)

#Q25. Check whether a number is even or odd.
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(12)

#Q26. Calculate area of a rectangle.
def area(length, width):
    print("Area =", length * width)

area(10, 5)

#Q27. Return the greater number.
def greater(a, b):
    if a > b:
        return a
    return b

print(greater(15, 25))

#Q28. Print numbers from 1 to 10.
def numbers():
    for i in range(1, 11):
        print(i)

numbers()

#Q29. Calculate sum of all numbers in a list.
def list_sum(lst):
    return sum(lst)

numbers = [10, 20, 30, 40, 50]

print("Sum =", list_sum(numbers))

#Q30. Check Pass or Fail.
def result(marks):
    if marks >= 35:
        print("Pass")
    else:
        print("Fail")

result(60)

#Q31. Function with default arguments (Default city = Pune).
def student(name, city="Pune"):
    print("Name:", name)
    print("City:", city)

student("Sham")
student("Rahul", "Mumbai")

#Q32. Function using keyword arguments.
def student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student(name="Sham", age=22, city="Pune")

#Q33. Accept multiple numbers using args.
def numbers(*args):
    for num in args:
        print(num)

numbers(10, 20, 30, 40, 50)

#Q34. Return Maximum and Minimum number from a list.
def max_min(lst):
    return max(lst), min(lst)

numbers = [10, 40, 5, 70, 25]

maximum, minimum = max_min(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)

#Q35. Count vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

string = input("Enter a string: ")

print("Total Vowels:", count_vowels(string))