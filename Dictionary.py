# 1. Create a Dictionary with at least 5 key-value pairs of the Student ID and Name
Dict = dict([(1, 'Jaya'), (2, 'Adhi'), (3, 'maha'), (4, 'Yamini'), (5, 'loki')])
print("1. Dictionary with each item as a pair:", Dict)  

# 2. Adding the values in the dictionary
Dict[6] = 'Nani'
print("\n2. Dictionary with a new item added:", Dict)  

# 3. Updating the values in the dictionary
Dict[3] = 'Mani'
print("\n3. Dictionary with updated values:", Dict)  

# 4. Accessing the value in the dictionary
print("\n4. Accessing one value in the Dictionary with key 1:", Dict[1])  

# 5. Creating a Nested Dictionary
Dict1 = {1: 'Jaya', 2: 'Adhi', 3: {'Age': 20, 'Branch': 'Ds', 'Year': 'Final Year'}}
print("\n5. Nested dictionary:", Dict1)  # Printing the nested dictionary
# 6. Access the values of nested loop dictionary
print("\n6. Accessing an element of the Nested Dictionary (Branch of ID 3):", Dict1[3]['Branch'])

# 7. Printing the keys present in a particular dictionary
print("\n7. Keys in the dictionary:", Dict.keys()) 

# 8. Delete a value from a dictionary

del Dict[6]
print("\n8. Dictionary after deleting a value with key 6:", Dict)  

