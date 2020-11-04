# # Let's create a greeting function
#
# def greeting():
#     print("Welcome on board ")
#
# # When we run this function, nothing happens. In order to execute a function, we must call it as shown:
# greeting()
# # Upon calling the function, the print statement is exectuted and we see "Welcome on board" printed to the console.
#
# # we can take this to the next level by taking arguments. These are values inside the parentheses. These arguments can be of any type and as much as we want.
# def greeting(name):
#     print("Welcome on board {}!".format(name))
#
# greeting("Harry")


# # Let's create a new funtion that takes two arguments as ints and add the value of the args
#
# def add(num1,num2):
#     print(num1+num2) # Takes the two arguments, adds them teogtehr and prints out to the console.
#
# # Now, we can call the function, making sure we supply **all** the required arguments.
# add(3,5)
# # We haven't restricted the function so it can take arguments in the form of floats...
# add(2,2.3)
# #  ... and strings.
# add("str","ing")

#  Creating a function to subtract 2 arguments
def subtract(num1,num2):
    print(num1-num2)

subtract(89,80)


# Practice Exercise-
# Create a function to multiply
def multiply(num1, num2):
    # Instead of using print, we can use return. This is a keyword which stop the execution of the program. Return stores the value, but does not ouput to the console.
    return num1*num2
# Create a function to divide
def divide(num1,num2):
    return num1/num2
# Create a function to %
def remainder(num1,num2):
    return num1%num2

multiply(5,3) # This won't print an output to the console
print(multiply(5,3)) # This will
