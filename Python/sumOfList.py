size = int(input("Enter How Many elements you want to: "))
a = []
for i in range(size):
    value = int(input("Enter the values of list"))
    a.append(value)
print("Original Array: ", a)
sum=0
for i in range(size):
    sum=sum+a[i]
print("Sum of List Elements= ", sum)
    