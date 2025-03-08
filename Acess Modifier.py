''' Create a class with PRIVATE fields, private method and a main method. Print the fields
in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class.'''


class Parent:
    def __init__(self):
        self.__private_field = "I am Private"  # Private field 

    def __private_method(self):
        """ Private method (Only accessible inside the Parent class) """
        return "This is a private method."

    def access_private_method(self):  
        """ Public method that allows access to the private method """
        return self.__private_method()

    def access_private_field(self):  
        """ Public method that allows access to the private field """
        return self.__private_field


# MAIN METHOD 
obj = Parent()
print("Accessing Private Field in Main Method:", obj.access_private_field())  #  Allowed
print("Accessing Private Method in Main Method:", obj.access_private_method())  # Allowed


'''
Create a class with PROTECTED fields and methods. Access these fields and methods
from any other class in the same package.
Also, Access the PROTECTED fields and methods from child class located in a different
package
Access the PROTECTED fields and methods from any class in different package'''



class Child(Parent):
    def access_parent_private(self):
        """ Trying to access the private field of Parent (will cause an error) """
        try:
            return self.__private_field  # Cannot access private field from subclass
        except AttributeError:
            return "Cannot access private field from subclass."

    def access_parent_private_method(self):
        """ Trying to access the private method of Parent (will cause an error) """
        try:
            return self.__private_method()  # Cannot access private method from subclass
        except AttributeError:
            return "Cannot access private method from subclass."


# TESTING PRIVATE FIELD AND METHOD ACCESS IN SUBCLASS
child_obj = Child()
print(child_obj.access_parent_private())  #  Not allowed
print(child_obj.access_parent_private_method())  #  Not allowed


'''Create a class with PUBLIC fields and methods.
Access the public methods and fields from any class in the same package or different
package.'''



class ProtectedExample:
    def __init__(self):
        self._protected_field = "I am Protected"  # Protected field (can be accessed in subclasses)
    
    def _protected_method(self):
        """ Protected method (Accessible within subclasses) """
        return "This is a protected method."


# Accessing Protected Members from the Same Package
obj_protected = ProtectedExample()
print("Accessing Protected Field in Same Class:", obj_protected._protected_field)  #  Allowed
print("Accessing Protected Method in Same Class:", obj_protected._protected_method())  # Allowed




class ChildProtected(ProtectedExample):
    def access_protected(self):
        """ Accessing protected members from a subclass """
        return f"Accessing from Child: {self._protected_field}, {self._protected_method()}"

# Create child object
child_protected_obj = ChildProtected()
print(child_protected_obj.access_protected())  #  Allowed (because it's protected, not private)

