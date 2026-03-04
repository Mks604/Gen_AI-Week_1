
#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The finally block lets you execute code, regardless of the result of the try- and except blocks.

n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")