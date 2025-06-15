s=input()
def fun(i):
    if i>=len(s):
        return 1
    #take
    a=fun(i+2)
    #not take
    b=fun(i+1)
    return a+b
print(fun(0)-1)
