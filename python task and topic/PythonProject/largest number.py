mylist = [10,30,15,3]
for x in range(len(mylist)):
  for i in range(len(mylist)-1):
    if mylist[i] > mylist[i+1]:
        temp = mylist[i]
        mylist[i] = mylist[i+1]
        mylist[i+1] = temp
        print(mylist)
