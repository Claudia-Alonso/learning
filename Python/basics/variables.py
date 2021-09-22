# Declare a variable and initialize it
# f = 0
# print(f)


# re-declaring the variable works
# f = "abc"
# print(f)


# ERROR: variables of different types cannot be combined
# print("this is a string" + 123) # Cannot concatenate 'str' and 'int' objects
print("this is a string " + str(123))


# Global vs. local variables in functions
# def someFunction():
#     f = "def"
#     print(f)

# someFunction()
# print(f) # name 'f' is not defined. Both 'f' variable are considered 2 different variables

def someFunction():
    global f # Defining this as global means we affet the f outside of the function
    f = "def"
    print(f)

someFunction()
print(f)

del f # Deletes the definition of a variable that was previously defined
print(f) # name 'f' is not defined
