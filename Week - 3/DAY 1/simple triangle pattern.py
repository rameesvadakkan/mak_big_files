"""
n = 6
for i in range(n):
    print("* "*(i+1) + " "*(n-1))

n = 6
for i in range(1,n+1):
    print(" "*(n-i) + "*"*i) """
n = 6 #pyramid and inverted and diamond
for i in range(n):
    print(" "*(n-i) + "*"*((2*i)+1))
for i in range(n,-1,-1):
    print(" "*(n-i) + "*"*((2*i)+1))

