def factorial(num):
    """Function to calculate the factorial of a given number"""
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
