a = []
for i in range(5):
    x=input("Enter Values: ")
    a.append(x)
print("Original Array: ", a)
index = int(input("Enter Index to Change: "))
value = input("Enter the value of Index: ")
a.insert(index,value)
print("After Change: ", a)

