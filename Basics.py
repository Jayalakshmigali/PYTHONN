# 1.Write a program to print your name

print("Jaya Lakshmi Gali")

# 2. Write a program for a Single line comment and multi-line comments


# This is Sinle Line Comment
print("Hello world")
''' This is Multi-line Comments
in python'''

# 3.Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

a=5
print("type of a:",type(a))
b=False
print("Type of b:",type(b))
c=5.0
print("Type of c:",type(c))
d="hello"
print("Type of d:",type(d))
e=3.1425
print("Type of e:",type(e))   # returns float

# 4.Define the local and Global variables with the same name and print both variables and understand the scope of the variable

x = 10     # Global variable

# Local variable with the same name
x = 20
print("Local variable x (after assignment):", x)

print("Global variable x:", x)
