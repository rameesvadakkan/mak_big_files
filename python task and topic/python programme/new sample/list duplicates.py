mylist = [10,20,15,15,30,20,9,4,80,100,9,10]
duplicates = set()
seen = set()

for x in mylist :
    if x in seen :
        duplicates.add(x)
    else:
        seen.add(x)
print(list(duplicates))        