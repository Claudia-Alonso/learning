# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x


# function with default value for an argument
def power(num, x=1): # If no x value given, x will be 1
    result=1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args): # The star character means I can pass in a variable number of arguments
    result=0
    for x in args:
        result=result+x
    return result # The function then loops over each argument and adds them all to a running total, which is then returned.

# func1()
# print (func1()) #Since func1() doesnt return any value, Python interprets this as 'None' and prints that
# print (func1) # Printing the value of the function definition. Functions are objects that can be passed around to other bits of Python code
# func2(10,20)
# print(func2(10,20))
# print(cube(3))
print(power(2))
print(power(2,3))
print(power(x=3, num=2)) 
# You don't have to call the function with the arguments in a particular order, 
#if you simply supply the names along with the values.
print(multi_add(4, 5, 10, 4))
print(multi_add(10, 4, 5, 10, 4))

# You can combine a variable argument list with a set of formal arguments, 
# but just keep in mind that the variable argument list always has to be the last parameter
