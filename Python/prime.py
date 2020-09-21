i = int(input("Enter any Number: "))
count = 0
n = 1
while n<=i:
    if i%n==0:
        count= count+1
    n = n+1

if count==2:
    print("Prime Number ")
else:
    print("Not Prime Number")
    
