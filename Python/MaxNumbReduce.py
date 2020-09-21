from functools import reduce
def myFunc(a,b):
    if a>b:
        return a
    else:
        return b
val=[1,2,3,4,5]
max=reduce(myFunc, val)
print("Max = ", max)
