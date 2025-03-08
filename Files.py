#1.Write a program to read text file
file=open("program.txt",'r')
data=file.read()
print(data)


# 2.Write a program to write text to .txt file using InputStream

file = open("program.txt", "w")

text = input("Enter text ")

file.write(text)#  input text to the file

# Close the file
file.close()
print("Text successfully written to output.txt")

# 3.Write a program to read a file stream

file = open("program.txt", "r")

content = file.read() # read the file
print("File Content:\n", content)

file.close()


#4.Write a program to read a file stream supports random access

file = open("program.txt", "r")

file.seek(5)
print("Reading from 5th character:", file.read(5))  

# Move back to the beginning
file.seek(0)
print("First line:", file.readline())  

file.close()


#Write a program to read a file a just to a particular index using seek()

file = open("program.txt", "r")
file.seek(10)
print("Content from 10th index:", file.read())
file.close()


# 6.Write a program to check whether a file is having read access and write access permissions
import os

def check_file_permissions(file_path):
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' does not exist.")
        return
    
    read_access = os.access(file_path, os.R_OK)
    write_access = os.access(file_path, os.W_OK)
    
    print(f"File: {file_path}")
    print(f"Read Access: {'Yes' if read_access else 'No'}")
    print(f"Write Access: {'Yes' if write_access else 'No'}")

file_path = input("Enter the file path: ")
check_file_permissions(file_path)