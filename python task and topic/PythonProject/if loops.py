#Print Even Numbers from 1 to 50
print("Even numbers")
for x in range(1,50):
    if x % 2 == 0 :
        print(x)

#Count How Many Numbers Are Divisible by 3 in a Given Range

n = 0
for i in range(1,30) :
    if i % 3 == 0 :
       n = n + 1

print(f"These are {n} the numbers divisible by 3 between 1 and 20")

#FizzBuzz Problem

for m in range(1,51):
    if m % 3 == 0 and m % 5 == 0:
        print("FizzBuzz")
    elif m % 3== 0 :
        print("Fizz")
    elif m % 5 == 0 :
        print("Buzz")

    else:
        print(m)
#Find the largest number of 3 numbers
print("Enter any Three numbers")
a=input()
b=input()
c=input()

