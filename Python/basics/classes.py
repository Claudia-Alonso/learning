class myClass(): 
    # Classes are defined using the class keyword and they are given a name
    # if this class was based on a superclass that I was inheriting from,
    # I would put the name of that other class, here inside these parentheses
    def method1(self): 
        # Usually, the first argument to any of the methods of a class, 
        # is the self argument and the self argument refers to the object itself. 
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)

class anotherClass(myClass): # anotherClass is inheriting from myClass
    def method1(self):
        myClass.method1(self) #  I'm inside the class one. So, now I do need to pass the self around when I use it. 
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 ")

def main():
    c = myClass() # Instantiating the class. Will instantiate an object instance of this class
    # I can then call methods in the class like I can call methods on any other object
    # when I call the class methods I don't have to supply the self keyword. 
    # That's automatically handled for me by the Python run time
    # I just have to care about the arguments that I'm passing in to each of the methods
    c.method1()
    c.method2("this is a sting")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string") 
    # Even though we're passing in an argument, the argument is not being used. 
    # So, it's not being printed and since we're not calling the inherited method, 
    # the argument is not being printed out in the myClass code

if __name__ == "__main__":
    main()
