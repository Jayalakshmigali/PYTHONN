# creating constructor and method
class Package:    
    class ClassOne:
        def __init__(self, name): # creation of __int__.py
            self.name = name  

        def show_message(self):
            print(f"Hello from ClassOne, {self.name}!")

    class ClassTwo:
        def __init__(self, age):
            self.age = age  

        def display_age(self):
            print(f"Your age is {self.age}.")

if __name__ == "__main__":
    # Creating objects and calling methods
    obj1 = Package.ClassOne("Alice")
    obj1.show_message()

    obj2 = Package.ClassTwo(25)
    obj2.display_age()
