#Question 1: Create a file named student.txt and write your name into it.

file = open("student.txt", "w")

file.write("Amit")

file.close()

print("Data written successfully.")

#Output

#Data written successfully.

#Question 2: Read data from student.txt.

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()

#Output

#Amit

#Question 3: Append your city name to the file.

file = open("student.txt", "a")

file.write("\nPune")

file.close()

print("City name appended successfully.")

#Output

#City name appended successfully.

#Contents of student.txt:

#Amit
#Pune

#Question 4: Read the file using readline().

file = open("student.txt", "r")

print(file.readline())
print(file.readline())

file.close()

#Output
#Amit
#Pune

#Question 5: Check whether a file exists or not.

import os

if os.path.exists("student.txt"):
    print("File exists.")
else:
    print("File does not exist.")

#Output

#File exists.

#Question 6: Store 5 student names in a file and display them.

students = ["Amit", "Rahul", "Priya", "Neha", "Karan"]

file = open("students.txt", "w")

for student in students:
    file.write(student + "\n")

file.close()

file = open("students.txt", "r")

print("Student Names:")
print(file.read())

file.close()

#Output

#Student Names:

#Amit
#Rahul
#Priya
#Neha
#Karan

