#Question 1: Handle Division by Zero

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

#Output

#Enter first number: 10
#Enter second number: 0
#Cannot divide by zero.

#Question 2: Handle Invalid Number Input

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input. Please enter a number.")

#Output

#Enter a number: abc
#Invalid input. Please enter a number.

#Question 3: Using try and except

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Index out of range.")

#Output

#Enter index: 10
#Index out of range.

#Question 4: Using else Block

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

#Output

#Enter first number: 20
#Enter second number: 4
#Result: 5.0

#Question 5: Using finally Block

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("File operation completed.")

#Output (if file is missing)

#File not found.
#File operation completed.

#Question 6: Multiple Exceptions

numbers = [10, 20, 30, 40, 50]

try:
    num = int(input("Enter a number: "))
    index = int(input("Enter index: "))

    print("Number:", num)
    print("Element:", numbers[index])

except ValueError:
    print("Invalid input.")

except IndexError:
    print("Index out of range.")

#Output 1

#Enter a number: abc
#Invalid input.

#Output 2

#Enter a number: 5
#Enter index: 10
#Index out of range.

#Question 7: Custom Exception

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError

    print("Number:", num)

except NegativeNumberError:
    print("Negative numbers are not allowed.")

#Output

#Enter a number: -5
#5Negative numbers are not allowed.