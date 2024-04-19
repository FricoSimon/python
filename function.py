# return string only
def greeting():
    return "Hello World"

print(greeting())

# return result from parameter
def multiply(a,b):
    return a*b

print(multiply(2,3))

# factorial challenge function
# still not correct
def factorial(number):
    result = 1
    for x in range(number):
        result *= x
    return result

print(factorial(5))