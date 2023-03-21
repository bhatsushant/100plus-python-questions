# Q24. Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

# And add document for your own function

def doc():
    '''The first function computes the power of the given function and the second function returns the absolute value of the integer'''
    print(pow(2,2))
    print(abs(-5))

print(doc())
print(doc.__doc__)