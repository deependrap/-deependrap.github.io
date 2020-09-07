n = int(input("Enter Any Number: "))
mul = 1
while n>0:
    mul = mul*(n%10)
    n=n//10
print("Product of Digit= ", mul)