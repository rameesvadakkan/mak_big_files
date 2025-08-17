n=6
"""for i in range(0,5): #pyramid
    for j in range(i,5):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(6): #inverted pyramid
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,6-1):
        print("*",end=" ")
    for j in range(i,6):
        print("*",end=" ")
    print()

for i in range(0,6-1): #diamond
    for j in range(i,6):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(6):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,6-1):
        print("*",end=" ")
    for j in range(i,6):
        print("*",end=" ")
    print() """

for i in range(n):
    for j in range(i+1):
        print("*"*2,end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()

