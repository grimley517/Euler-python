def nterm(a,b):
    return (a+b)
    
def fiblist(target):
    answer = [1]
    nt = 2
    while nt<target:
        answer.append(nt)
        nt = nterm(answer[-1],answer[-2])
    return (answer)

def fiblisteven1(target):
    answer = fiblist(target)
    for item in answer:
        if item % 2 == 1:
            answer.remove(item)
    return(answer)

def fiblisteven2(target):
    startlist = fiblist(target)
    answer = []
    for item in startlist:
        if item % 2 == 0:
            answer.append(item)
    return(answer)

def sumof(alist):
    return (sum(alist))