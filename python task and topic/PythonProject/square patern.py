'''
for i in range(6): #Right-angled triangle (left-aligned)
    for j in range(0,6) :
        if j < i :
            print("*",end=" ")
    print()

for i in range(6): #inverted Right-angled triangle (left-aligned)
    for j in range(6) :
        if j > i :
            print("*",end=" ")
    print()
r=5
for i in range(1,r+1): #Right-angled triangle (right-aligned)
    for j in range(r-i):
        print(" ",end=" ")
    for star in range(i):
        print("*",end=" ")
    print()
r=5
for i in range(r): #Right-angled triangle (left-aligned)
    for j in range(i):
        print(" ",end=" ")
    for star in range(r-i):
        print("*",end=" ")
    print()
rows = 5
for i in range(1,rows+1):
    for space in range(rows-i):
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print()
rows = 5
for i in range(rows):
    for space in range(i):
        print(" ",end="")
    for star in range(2*(rows-i)-1):
        print("*",end="")
    print()'''
