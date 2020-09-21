eng = int(input("Enter Marks of English Subject"))
nep = int(input("Enter Marks of Nepali Subject"))
math = int(input("Enter Marks of Mathematics Subject"))
sci = int(input("Enter Marks of Science Subject"))
health = int(input("Enter Marks of Health Subject"))

total = eng+nep+math+sci+health
percent = (total*100)/500

if percent>80:
    print("Congratulation! You are passed. Total Marks obtained:", total, "Percentage", percent, "Grade: A")
elif percent>=60:
        print("Congratulation! You are passed. Total Marks obtained:", total, "Percentage", percent, "Grade: B")
elif percent>=40:
        print("Congratulation! You are passed. Total Marks obtained:", total, "Percentage", percent, "Grade: C")
else:
    print("Sorry! You are failed. Total Marks obtained:", total, "Percentage", percent, "Grade: C")

        

