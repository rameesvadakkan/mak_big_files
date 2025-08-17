x = lambda a : a+10
print(x(5))

y = lambda b : b*10
print(y(10))

z = lambda c,e : c*e
print(z(20,90))

def myfun(n):
    return lambda a:a*n
mydoubler=myfun(3)
print(mydoubler(10))
