str1="apple"
str2="Apple"
if str1==str2 :
    print("apple and Apple equal") #not equal, because Python is case-sensitive
elif str1.lower() == str2.lower(): #convert both to lowercase (or uppercase)
    print(str1.lower() == str2.lower())

    print(str1==str2)
