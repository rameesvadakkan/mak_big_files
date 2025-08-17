while True :
    number = input("Enter a number: ")
    try:
        number = float(number)
        break
    except ValueError:
        print("Enter a valid value,please try again")
if number % 2 == 0:
    print("Its is a Even number")
else :
    print("Number is Odd")
