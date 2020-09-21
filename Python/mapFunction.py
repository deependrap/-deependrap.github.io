ages=[5,12,17,18,24,32]
def myfunc(a):
    if a%2==0:
        return True
    else:
        return False
def squ(a):
    return a*a
val=list(filter(myfunc, ages))
squres=list(map(squ,val))
for x in val:
    print(x, end=" ")
for y in squres:
    print(y, end=" ")
    

