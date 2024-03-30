# Basic function to add two numbers and return the sum

def num_adder(a, b):
    c = a + b
    return c

# Calling this function with the numbers 5 and 7

num_adder(5, 7)

# Function to add two numbers with no return statement

def no_return(a, b):
    c = a + b

# Calling the function with the numbers 5 and 7 to illustrate that without a return statement the function will not yield output

no_return(5, 7)

# We'll now assign to variable c the return of the num adder function so that it will be defined in global scope

c = num_adder(5, 7)

# Validating that the variable c is now assigned the return of the num_adder function

c

# Basic function to add three numbers and return the sum

def three_num_adder(a, b, c):
    return a + b + c

# Calling the function with the numbers 5, 7, and 11

three_num_adder(5, 7, 11)

# Basic function to concatenate two strings

def string_adder(string1, string2):
    statement = str(string1) + str(string2)
    return statement

# Calling the function with the arguments 'hello' and ' world'

string_adder('hello', ' world')

# Basic function using *args to illustrate how to build a function that can take an unknown number of arguments. This function adds all the arguments 
# and returns the sum

def args_adder(*args):
    sum = 0
    for num in args:
        sum += num
    return sum 

# Calling the function with 7 arguments to illustrate that this function will accept any number of arguments

args_adder(5, 7, 11, 23, 31, 45, 111)

# Basic function that accepts an unlimited number of string arguments and concatenates them into one statement 

def args_string_adder(*strings):
    statement = ''
    for string in strings:
        statement += string
    return statement

# Calling the function with 5 arguments to illustrate that the concatenation works

args_string_adder('wow,', ' does', ' this', ' really', ' work?')

# Function to concatenate all the keyword values into a statement

def dict_value_unpacker(**kwargs):
    statement = ''
    for key, value in kwargs.items():
        statement += value
    return statement

# Calling this function to validate that it will concatenate string values

dict_value_unpacker(string1 = 'this', string2 = ' is', string3 = ' cool!')

# Function that returns a dictionary of the key:value pairs of the arguments

def dict_builder(**kwargs):
    return kwargs

# Calling this function to validate that it returns a dictionary of the arguments

dict_builder(string1 = 'this', string2 = ' is', string3 = ' cool!')

# Calling the args_adder function passing the result of num_adder function as arguments

args_adder(num_adder(5, 7), num_adder(3, 8), num_adder(4, 11))

# Function args_subtracter calls function num_adder within it's block which adds a and b and saves it to the variable result then subtracting 10 from 
# the return of num_adder and overwriting that to the variable of result

def args_subtracter(a, b):
    result = num_adder(a, b)
    result -= 10
    return result

# Calling the function to illustrate that it acts as we would expect returning 17 when passed 12 and 15 because 12 + 15 - 10 = 17

args_subtracter(12, 15)

# Declaring a function that takes any number of integer arguments, adds them together saving the result in the variable sum. Sum is then evaluated
# against 100 assigning the string 'Sum is greater than 100' if that is the case to the variable result and 'Sum is less than or equal to 100' if that
# is not the case

def greater_than_100(*nums):
    sum = 0
    for i in nums:
        sum += i
    if sum > 100:
        result = 'Sum is greater than 100'
    else:
        result = 'Sum is less than or equal to 100'
    return result

greater_than_100(4, 13, 67)

greater_than_100(101)

