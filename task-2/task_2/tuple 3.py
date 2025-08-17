mytuple =("apple","orange","mango")
print(mytuple)
newvalue=list(mytuple)
newvalue[1]="grape"
newvalue.append("cherry")
mytuple = tuple(newvalue)
print(mytuple)



