# Functions in Python
This lesson will cover Python Functions

## What are functions and why are they useful?
**DRY - Don't Repeat Yourself**
* This is a key mantra in Python, we don't want to constantly retype something. 
* Instead we can call a function to carry out a repetitive action for us. 

## How to create a function
Syntax: 
```def <name_of_function>():```

### Return statements
* We use return statements to return the result of any function. 
* This is a keyword which stop the execution of the program. Return stores the value, but does not output to the console.

### Example 1
* Let's create a greeting function. This is one of the most basic functions, it prints "Welcome on board"
```python
def greeting():
    print("Welcome on board ")
```
When we run this function, nothing happens. In order to execute a function, we must call it as shown:
```python
greeting()
```
* Upon calling the function, the print statement is executed and we see "Welcome on board" printed to the console.

* We can take this to the next level by taking arguments. These are values inside the parentheses. These arguments can be of any type and as much as we want.
```python
# This function takes one argument, name
def greeting(name):
    # We want to print a message saying "Welcome on board <user name>". 
    print("Welcome on board {}!".format(name))

# We must then call the function, making sure we supply the argument. 
greeting("Harry")
```

## Example 2
* Let's create a new funtion that takes two arguments as ints and add the value of the args
* First we define the function and we want two arguments as this is the what we want the function to do, take two numbers and add them
```python
def add(num1,num2):
     print(num1+num2) # Takes the two arguments, adds them together and prints out to the console.
```
* Now, we can call the function, making sure we supply **all** the required arguments.
```python
add(3,5)
 # We haven't restricted the function so it can take arguments in the form of floats...
add(2,2.3)
#  ... and strings.
add("str","ing")
```
* We can repeat this process to carry out other arithmetic operators such as subtract, multiply, divide and calculate the remainder: 
1. Subtract
```python
#  Creating a function to subtract 2 arguments
def subtract(num1,num2):
    print(num1-num2)

subtract(89,80)
```
2. Multiply 
```python
# Create a function to multiply
def multiply(num1, num2):
    return num1*num2
```
* In this example, instead of using print, we have used return. 

3. Divide 
```python
# Create a function to divide
def divide(num1,num2):
    return num1/num2
```
4. Remainder 
```python
# Create a function to %
def remainder(num1,num2):
    return num1%num2
```

* In each of these functions, we have not called the function so there is no output. As before, we call the function, ensuring we supply all arguments
```python
multiply(3,4) # Returns 12
divide(9,3) # Returns 2
remainder(14,3) # Returns 2 
```
* HOWEVER, for these functions, we used to return keyword. This does not print to the console so we must specify that we want to print.
```python
print(multiply(4,3)) # Prints 12
print(divide(9,3)) # Prints 3
print(remainder(14,3)) # Prints 2
```





## Best Practices
* Have a small block of code in any function that does one job.
* Use pseudocode - one line of explanation is sufficient.
* HINTs: Create hints in simple bullet points.
* Comments regarding your function results
