def mults(multiplier, target):
    answer = []
    number = 0
    while (number+multiplier < target):
        number += multiplier
        answer.append(number)
    return (answer)
    
def sumof(alist):
    answer = 0
    for i in alist:
        answer +=i
    return (answer)