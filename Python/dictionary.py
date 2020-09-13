student_DB = {}
# input
while True:
    line = input("Enter the Student ID and Name separated by comma or q for exit: ")
    if line=='q':
        break
    id, name = line.split(',')
    student_DB.update({id:name})
# output
for x, y in student_DB.items():
    print(x, y)

# Searching
key = input("Enter ID of Student to Search: ")
if key in student_DB:
    print("Key ", key, "Student Name: ", student_DB[key])
else:
    print("Not Found! ")
