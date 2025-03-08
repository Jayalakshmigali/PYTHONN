1.#Different ways creating a string
string='Hello'
print(string)

string1="world"
print(string1)

string3='''python'''
print(string3)

string4=""" Hello
world"""
print(string4)


# 2.Concatenating two strings using + operator
str1='hello'
str2='world'
print(str1+str2)

# 3.Finding the length of the string
str5='Python'
print(len(str5))

# 4.Extract a string using Substring
string = "Hello  Python!"
substring = string[7:13]  
print(substring)  


#5.Searching in strings using index()
string = "Welcome to Python "
index = string.index("Python")  # Finds the index where "Python" starts
print("Index of 'Python':", index)

#6.Matching a String Against a Regular Expression With matches()

import re
Substr = 'Madras'
str6 = 'Madras once called as madaras'
print(re.match(Substr,str6))
print()


# 7.Comparing strings
str1 = 'Jaya'
str2 = 'adya'
str3 = str1
print(str2 == str1)
print(str3 == str2)
print(str1 == str3)
print(str2 != str1)
print()


# 8.startsWith(), endsWith() and compareTo()
string = 'Jaya Lakshmi Gali'
print(string.startswith("Ja"))
print(string.endswith("aya"))
print()

# 9.Trimming strings with strip()
str0="Welcome To Python ^&"
print(str0.strip('&'))

# 10.Replacing characters in strings with replace()
str1='Greetings To Python'
print(str1.replace('Greetings','Welcome'))
print()

# 11.Splitting strings with split()
string = 'hey^hello*python'
print(string.split("*"))
print()

# 12.Converting integer objects to Strings
number = 99
number1 = str(number)
print(number1)
print(type(number1))

# 13.Converting to uppercase and lowercase
str1 = 'Welcome To'
str2 = 'PYthon'
print(str1.upper())
print(str2.lower())