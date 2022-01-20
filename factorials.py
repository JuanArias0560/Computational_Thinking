

def factorial(n):
    """compute the factorial of n
    n int > 0 
    returns n!

    """
    print(n)
    if n ==1 :
        return 1
    
    return n * factorial(n-1)

n =int(input('write a inter number: '))

print(factorial(n))
