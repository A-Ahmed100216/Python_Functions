# BASIC FUNCTION
# Create a greeting function
def greeting():
    print("Welcome on board ")

# In order to execute a function, we must call it as shown:
greeting() # Prints "Welcome on board"


# ADDING ARGUMENTS
def greeting(name):
    # We want to personalise the greeting so we can format the print statement to take into account the name argument.
    print("Welcome on board {}!".format(name))
# Call the function
greeting("Harry")
#  Prints "Welcome on board Harry!"


# ADDITION FUNCTION
# Let's create a new function that takes two arguments and add the value of the args.
def add(num1,num2):
    # Takes the two arguments, adds them together and prints out to the console.
     print(num1+num2)

# Call the function, making sure we supply all the required arguments.
add(3,5)
# We haven't restricted the function so it can take arguments in the form of floats...
add(2,2.3)  # Returns 4.3
#  ... and strings.
add("str","ing")   # Returns string

# SUBTRACT FUNCTION
#  Creating a function to subtract 2 arguments
def subtract(num1,num2):
     # Instead of using print, we can use return.
     return num1-num2

#Call the function
subtract(89,80)

#We can assign the function to a variable
subtracted_value= subtract(89,80)
print(subtracted_value)


# TASK-BASIC CALCULATOR
# Implement the return keyword.
# Create a function to multiply, divide and find the remainder of two integer arguments.
def multiply(num1, num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def remainder(num1,num2):
    return num1%num2

# Call the functions
multiply(5,3)  # This won't print an output to the console as the function uses the return keyword
print(multiply(5,3))  # This will - prints 15
print(divide(15,3))  # Prints 5
print(remainder(14,3))  # Prints 2

