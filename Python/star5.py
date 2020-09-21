n=int(input("Enter the number for row: "))
k=1
i=1
while i<=n:
    b=1
    while b<=n-i:
        print(" ", end='')
        b=b+1
    j=1
    while j<=k:
        print(i, end='')
        j=j+1
    print()
    k=k+2
    i=i+1
    