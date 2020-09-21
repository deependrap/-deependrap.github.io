ages=[5,12,17,18,24,32]
adult=filter(lambda a: a>18, ages)
squ=list(map(lambda a: a*a, adult))
print(squ)
