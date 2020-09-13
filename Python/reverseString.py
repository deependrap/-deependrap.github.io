a = []
n = int(input("Enter the length of List"))
for i in range(n):
    x = input("Enter the Values: ")
    a.append(x)
print("Original List: ", a)
# a.pop()
# print(a)

# a.sort()
# print(a)

a.reverse()
print("After reverse List is ", a)