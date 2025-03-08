''' 1.Write a class with a default constructor, one argument constructor and two argument
constructors. Instantiate the class to call all the constructors of that class from a main
class'''

class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor Called")
        elif arg2 is None:
            print(f"One Argument Constructor Called: arg1 = {arg1}")
        else:
            print(f"Two Argument Constructor Called: arg1 = {arg1}, arg2 = {arg2}")

# Main class to instantiate MyClass and call all constructors
if __name__ == "__main__":
    obj1 = MyClass()           # Calls default constructor
    obj2 = MyClass(10)         # Calls one argument constructor
    obj3 = MyClass(10, 20) 


# 2.Call the constructors(both default and argument constructors) of super class from a child class

class SuperClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("SuperClass Default Constructor Called")
        elif arg2 is None:
            print(f"SuperClass One Argument Constructor Called: arg1 = {arg1}")
        else:
            print(f"SuperClass Two Argument Constructor Called: arg1 = {arg1}, arg2 = {arg2}")

class ChildClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        super().__init__(arg1, arg2)
        print("ChildClass Constructor Called")

# Main class to instantiate ChildClass and call all constructors
if __name__ == "__main__":
    obj1 = ChildClass()           # Calls default constructor 
    obj2 = ChildClass(10)         # Calls one argument constructor 
    obj3 = ChildClass(10, 20)     # Calls two argument constructor 


#3.Apply private, public, protected and default access modifiers to the constructor

class SuperClass:
    def __init__(self):
        print("SuperClass Public Constructor Called")

    def _protected_constructor(self, arg1):
        print(f"SuperClass Protected Constructor Called: arg1 = {arg1}")

    def __private_constructor(self, arg1, arg2):
        print(f"SuperClass Private Constructor Called: arg1 = {arg1}, arg2 = {arg2}")

    @classmethod
    def create_protected(cls, arg1):
        instance = cls.__new__(cls)
        instance._protected_constructor(arg1)
        return instance

    @classmethod
    def create_private(cls, arg1, arg2):
        instance = cls.__new__(cls)
        instance.__private_constructor(arg1, arg2)
        return instance

class ChildClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        super().__init__()
        if arg1 is not None and arg2 is None:
            self._protected_constructor(arg1)
        elif arg1 is not None and arg2 is not None:
            self.__private_constructor(arg1, arg2)
        print("ChildClass Constructor Called")

# Main class to instantiate ChildClass and call all constructors
if __name__ == "__main__":
    obj1 = SuperClass()              # Calls public constructor
    obj2 = SuperClass.create_protected(10)   # Calls protected constructor
    obj3 = SuperClass.create_private(10, 20) # Calls private constructor


# 4.Write a program which illustrates the concept of attributes of a constructor.

class MyClass:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age   # Protected attribute
        self.__id = 1001  # Private attribute
        print("Constructor is called and attributes are initialized")
    
    def display_attributes(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"ID: {self.__id}")

# Main class to instantiate MyClass and illustrate constructor attributes
if __name__ == "__main__":
    obj = MyClass("Alice", 25)
    obj.display_attributes()
    
    print(f"Accessing Public Attribute: {obj.name}")
    print(f"Accessing Protected Attribute: {obj._age}")
    
    print(f"Accessing Private Attribute via Name Mangling: {obj._MyClass__id}")