# 1.Write a function for arithmetic operators(+,-,*,/)

num1=int(input("enter a number"))
num2=int(input("enter a number"))
add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
print("addition is:",add)
print("difference is:",sub)
print("product is:",mul)
print("division is:",div)

# 2.Write a method for increment and decrement operators(++, --)

a = 0  
a += 1  # Increment by 1
a = a + 1  
print('The value of a is', a)

print("INCREMENTED FOR LOOP")# starts from 0
for i in range(0, 5):  # Loops from 0 to 4
   print(i)

print("\nDECREMENTED FOR LOOP")# starts from 4
for i in range(4, -1, -1):  # Loops from 4 to 0
   print(i)


# 3.Write a program to find the two numbers equal or not.

a=input("enter")
b=input("enter")
if a==b:
    print("equal")
else:
    print("not equal")   

#4.Program for relational operators (<,<==, >, >==)

a=4
b=5
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b) 

#5. Print the smaller and larger number

a=float(input("enter a number"))
b=float(input("enter a number"))
if a>b:
    print("a is big",a)
else:
    print("b is big",b)    

