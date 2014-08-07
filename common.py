import math
import itertools

def isPrime(n):
    '''
    tests an integer n for primeness
    '''
    if n<=1:
        return(False)
    elif n==2:
        return (True)
    else:
        top = math.ceil(math.sqrt(n))
        for i in range (2,top):
            if n%i == 0:
                return (False)
        return True

def combinations(n,r):
    '''returns the combinations of n things of r objects'''
    n= list(range(n))
    return(list(itertools.combinations(n,r)))
