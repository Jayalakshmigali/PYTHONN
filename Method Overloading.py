# 1.delWrite two methods with the same name but different number of parameters of same type and call the methods
class MyClass:
    def show(self, *args):
        if len(args) == 1:
            print(f"Method with one parameter: {args[0]}")
        elif len(args) == 2:
            print(f"Method with two parameters: {args[0]}, {args[1]}")
        else:
            print("Invalid number of arguments")

# Main execution
if __name__ == "__main__":
    obj = MyClass()
    obj.show(10)       # Calls method with one parameter
    obj.show(10, 20)   # Calls method with two parameters


# 2.Write two methods with the same name but different number of parameters of different data type and call the methods

class MyClass:
    def show(self, value=None, extra=None):
        if isinstance(value, int) and extra is None:
            print(f"Method with integer parameter: {value}")
        elif isinstance(value, str) and extra is None:
            print(f"Method with string parameter: {value}")
        elif isinstance(value, int) and isinstance(extra, str):
            print(f"Method with integer and string parameters: {value}, {extra}")
        else:
            print("Invalid parameter combination")

# Main execution
if __name__ == "__main__":
    obj = MyClass()
    obj.show(10)         # Calls method with an integer parameter
    obj.show("Hello")    # Calls method with a string parameter
    obj.show(20, "World")  # Calls method with integer and string parameters


# 3.Write two methods with the same name and same number of parameters of same type
class MyClass:
    def show(self, value):
        if isinstance(value, int):
            print(f"Method with integer parameter: {value}")
        elif isinstance(value, str):
            print(f"Method with string parameter: {value}")
        else:
            print("Invalid parameter type")

# Main execution
if __name__ == "__main__":
    obj = MyClass()
    obj.show(10)       # Calls method with integer parameter
    obj.show("Hello")  # Calls method with string parameter
