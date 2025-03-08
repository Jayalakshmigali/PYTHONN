# 1. Write a function to add integer values of an array
arr=[1,2,3,4]
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
print("sum of all integer values in array is:",sum)

# 2. Write a function to calculate the average value of an array of integers
num=[45,6,7,8,9,0,98,76]
total=0
for i in num:
    total=total+i
avg=total/len(num)
print("the average is:",avg)    

# 3.Write a program to find the index of an array elements
arr=[1,9,2,8,3,7,4,6,5]

index=arr.index(5)
print("index of 5 is", index)  

# 4.Write a function to test if array contains a specific value
arr=[1,10,4,2,9,3,8,4,7,5,6]
for n in arr:
         if n==6:
             print(n , "exists")

# 5.Write a function to remove a specific element from an array
arr=[11,34,5,67,89]
arr.remove(67)
print(arr)

#6.Write a function to copy an array to another array
arr = ['j','a','y','a']
arr1 = [] #creating empy array
arr1 = arr.copy() 
print(arr1)

#7.Write a function to insert an element at a specific position in the array
arr=[21,34,56,90,65]
arr.insert(1,24)
print(arr)

#8.Write a function to find the minimum and maximum value of an array
arr=[10,99,87,79,57,67]
minimum = min(arr)
print("The minimum is",minimum)
maximum=max(arr)
print("The maximum is",maximum)


# 9.Write a function to reverse an array of integer values
arr=[21,34,56,78,9,0]
arr.reverse()
print(arr)


arr=[6,7,8,9,10]
arr.reverse()
print(arr)

# 10.Write a function to find the duplicate values of an array
 
arr=[23,44,55,67,44,98,66,55]
for i in range(0,len(arr)):
    for k in range(i+1,len(arr)):
        if arr[i]==arr[k]:
            print("Duplicates are:",arr[k])


# 11.Write a program to find the common values between two arrays
arr=['j','a','y','a','l','a','k','s','h','m','i']
arr1=['j','a','i']
print("common Values are:",set(arr).intersection(arr1))

# 12.Write a method to remove duplicate elements from an array
arr=[23,45,67,23,78,67,98]
finalarr=[]
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)    

# 13.Write a method to find the second largest number in an array
arr=[998,567,789,456,345,234,123,879]
arr.sort()
print("Second Largest is:",arr[-2])


# 14.Write a method to find the second smallest number in an array
arr=[998,567,789,456,345,234,123,879]
arr.sort()
print("Second smallest is:",arr[1])

# 15.Write a method to find number of even number and odd numbers in an array
arr=[1,2,4,5,6,7,856,78,45,34,77]
even=0
odd=0
for i in arr:
    if i%2==0:
        even =even+1
    else:
        odd=odd+1
print("Even Numbers are:",even)
print("odd Numbers are:",odd)            


# 16.Write a function to get the difference of largest and smallest value
arr=[24,56,78,90,45,76]
arr.sort()
diff=arr[5]-arr[0]
print("Difference is:",diff)

# 17.Write a method to verify if the array contains two specified elements(12,23)
arr=[11,15,12,56,23,55,67]
for i in arr:
    if i==12 or i==23:
        print("Elements Exist")


#Write a program to remove the duplicate elements and return the new array
arr=[57,78,67,23,57,78,9]
finalarr=[]
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)        