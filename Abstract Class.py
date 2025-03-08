from abc import ABC, abstractmethod

# 1. Create an abstract class with an abstract method and a non-abstract method.
class Polygon(ABC):
    
    @abstractmethod
    def noofsides(self):
        pass
    def area(self):
        print("This is a general area method for all polygons.")

# 2. Create a subclass and access both abstract and non-abstract methods.
class Triangle(Polygon):
    
    def noofsides(self):
        print("Triangle: I have 3 sides")

    def get_area(self):
        self.area()
        print("Area of Triangle")

# 3. Create another subclass and call both methods (abstract and non-abstract).
class Pentagon(Polygon):
    
    def noofsides(self):
        print("Pentagon: I have 5 sides")
    
    # Using the non-abstract method from the parent class
    def get_area(self):
        self.area()
        print("Area of Pentagon")

# 4. Create another subclass and call both methods.
class Hexagon(Polygon):
    
    # Overriding the abstract method
    def noofsides(self):
        print("Hexagon: I have 6 sides")
    
    # Using the non-abstract method from the parent class
    def get_area(self):
        self.area()
        print("Area of Hexagon")
        
triangle = Triangle()
triangle.noofsides()  # Call abstract method
triangle.get_area()   # Call non-abstract method

# Pentagon
pentagon = Pentagon()
pentagon.noofsides()  # Call abstract method
pentagon.get_area()   # Call non-abstract method

# Hexagon
hexagon = Hexagon()
hexagon.noofsides()   # Call abstract method
hexagon.get_area()  