import math

def isPrimne(n):
    '''
    tests an integer n for primeness
    '''
    top = math.ceil(math.sqrt(n))
    for i in range (2,top):
        if n%i == 0:
            return False
    return True
    
