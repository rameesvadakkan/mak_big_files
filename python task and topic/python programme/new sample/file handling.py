#t = input("Enter texts :")

file = open("mylife.txt","r")
newfile = open("copymylife.txt","w")
content = file.read()
newfile.write(content)

file.close()
newfile.close()
print("succses")

