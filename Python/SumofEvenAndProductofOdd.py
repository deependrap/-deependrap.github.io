i=int(input("Enter Number: "))
sum=0
product=1
while i>0:
    d=i%10
    if i%2==0:
        sum=sum+d
    else:
        product=product*d
    i=i//10
print("Sum of even digit= ",sum,"Product of odd digit= ",product)
