# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

def evenOdd(x):          #syntax for function
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))