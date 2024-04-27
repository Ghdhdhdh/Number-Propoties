import math
from decimal import Decimal, getcontext


def absolute(n):
    """
    Returns the Absolute value of a number
    """
    return abs(n)

def negitive(n):
    """
    Returns if a number is negitive (True) or Positive (False)
    """
    return abs(n) != n

def power_of_2(n):
    """
    Returns if the number is a power of 2, in which case it will return the log2 of it, else, it'll return false

    """
    if (math.log(n)/math.log(2)).is_integer():

        # Is a power of 2
        return math.log2(n)
    else:
        #Not a power
        return False
    
def factors(n):
    """
    Finds all factors of a number and returns as a list
    """
    factors = []
    for factor in range(1, n + 1):
        if n % factor == 0:
            factors.append(factor)
    return factors

def multipliers(n):
    """
    Takes th facotrs and turns them into a x*y format:
    e.g  input 8 output: {8:1, 4:2, 2:4, 1:8}
    """

    factor = factors(n)
    multiples = {}
    for i in range(len(factor)):
        multiples[factor[i]] = factor[len(factor) - 1 - i]
    
    return multiples

def power_of_3(n):

    """
    Returns if the number is a power of 3, in which case it will return the log3 of it, else, it'll return false

    """
    j = 1
    i = 0

    while i < 10001:
        j *= 3
        i += 1
        if j == n:
            return i
        else:
            pass
    else:
        return False
    

    
