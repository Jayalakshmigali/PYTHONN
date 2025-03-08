# 1.Write a program to generate Arithmetic Exception without exception handling

result = 10/0 
print(result)  

# 2.Handle the Arithmetic exception using try-catch block

try:
    result = 10 / 0  
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")


# 3.Write a method which throws exception, Call that method in main class without try block

class MyClass:
    def throw_exception(self):
        raise ValueError("This is a manually thrown exception!")

# Main class execution
obj = MyClass()
obj.throw_exception()  

# 4. Write a program with multiple catch blocks
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2  # May cause ZeroDivisionError
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter a number.")

print("Program execution completed.")


# 5.Write a program to throw exception with your own message

num = int(input("Enter a number: "))

if num < 0:
    raise ValueError("Invalid input! Negative numbers are not allowed.")

print("You entered:", num)


# 6.Write a program to create your own exception

class NegativeNumberError(Exception):
    pass
num = int(input("Enter a positive number: "))

if num < 0:
    raise NegativeNumberError("Error: Negative numbers are not allowed!")
print("You entered:", num)


# 7.Write a program with finally block
try:
    print(10 / 0)  
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("This is the finally block")


# 8.Write a program to generate Arithmetic Exception
result=10/0
print(result)

# 9.Write a program to generate FileNotFoundException 
file=open('employee.txt','r')
print(file.read())
file.close()


# 10.Write a program to generate ClassNotFoundException
try:
    class NonExistentClass:  
        pass
    del NonExistentClass  

    obj = NonExistentClass() 
except NameError:
    print("Error: The Class was not found!")


# 11.Write a program to generate IOException
try:
    file = open("/root/restricted_file.txt", "w")  
except OSError:
    print("Error: An I/O Exception occurred!")

# 12. Write a program to generate NoSuchFieldException
class Employee:
    def __init__(self):
        self.name = "Jaya"
        self.age = 21

emp = Employee()

print(emp.salary)  
