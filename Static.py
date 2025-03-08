# 1. Define a static variable and access that through a class
class Python:
 staticVariable = 4 # Acess through Class
print(Python.staticVariable)


# 2.Define a static variable and access that through a instance
class python:
    staticVariable=34
instance=python    
print(instance.staticVariable)


# 3.Define a static variable and change within the instance
class python:
    staticVariable=78
instance=python()
instance.staticVariable=45
print(instance.staticVariable)
print(python.staticVariable)



# 4. Define a static variable and change within the class
class python:
    staticVariable=19
python.staticVariable = 89
print(python.staticVariable) 
 