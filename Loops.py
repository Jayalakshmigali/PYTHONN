# 1.Write a program to print “Bright IT Career” ten times using for loop

a="Bright IT Career"
for i in range(10):
    print(a)


# 2.Write a python program to print 1 to 20 numbers using the while loop.
i=1
while(i<=20):
    print(i)
    i=i+1

# 3.Program to equal operator and not equal operators
a = 5
b = 10
print(a ==b) #Equal operator
print(a != b) #Not Equal operator

#4.Write a program to print the odd and even numbers.
Numbers = [1,2,3,4,5,6,7,8,9,10]
print("Even Numbers: ")  
for i in Numbers:     
    if i % 2 == 0:       
        print(i, end =" ")    
print("\nOdd Numbers:")
for i in Numbers:
    if i % 2 != 0:
        print(i, end =" ")
print()


#5.Write a program to print largest number among three numbers.
a=input()
b=input()
c=input()
if a>=b and a>=c:
    largest=a
elif b>=c and b>=a:
    largest=a
else:
    largest=c
print("largest num is:",largest)        


    
# 6.Write a program to print even number between 10 and 20 using while
num=10
print("Even numbers between 10 & 20 are:")
while num<=20:
    if num%2==0:
        print(num,end=" ")
    num=num+1
print()

#7.Write a program to print 1 to 10 using the do-while loop statement.
num=1
print("numbers from 1 to 10")
while True:
    print(num)
    num=num+1
    if num>10:
        break


#8.Write a program to find Armstrong number or not
n=int(input("Enter a number"))
temp=n
sum=0
while n>0:
    dig=n%10
    sum= sum+(dig**3)
    n=n//10
if temp==sum:
    print(temp,"is an Armstrong Number")
else:
    print(temp,"is Not an armstrong Number")   


# 9.Write a program to find the prime or not.
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print(n,"is a Prime Number") 
else:
    print(n,"is Not a Prime Number")  


# 10.Write a program to palindrome or not.
n=input()
if n==n[::-1]:
    print(n,"is a Palindrome")
else:
    print(n,"is Not a Palindrome")    

# 11.Program to check whether a number is EVEN or ODD using switch
n=int(input("enter a Number"))
match n%2:
    case 0:
        print(n," is Even Number")
    case 1:
        print(n,"is odd Number")


# 12.Print gender (Male/Female) program according to given M/F using switch
char = input("Enter M or F: ").upper()  

switch = {
    "M": "Male",
    "F": "Female"
}
print(switch.get(char, "Invalid Input")) 

