i = int(input("Enter number for checking armstrong"))
sum = 0
orig = i
while(i>0):
    sum = sum+(i%10)*(i%10)*(i%10)
    i = i//10
if(orig==sum):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
