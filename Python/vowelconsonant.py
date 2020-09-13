a = input("Enter any Strings")
vowel = 0
conso = 0
for i in range(0,len(a)):
    if(a[i]!=" "):
        if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or
        a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
                    vowel=vowel+1
        else:
            conso=conso+1
print("Total Vowel= ", vowel)
print("Total Consonant= ", conso)
