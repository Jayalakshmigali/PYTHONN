class A:  
    def display(self):  
        print("Display Inside class A")

    # class A show method    
    def show(self):
        print("Show Inside class A")


class B(A): 
    def print(self):  
        print("Print Inside class B")    

    # class B show method
    def show(self):
        print("Show Inside class B")


class C(B):  
    # class C show method
    def show(self):
        print("Show Inside class C")         

# Driver Code
s = A()
s.display()  

k = B()
k.print() 

g = C()   
g.show()  

