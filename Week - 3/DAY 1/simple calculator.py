num1 = float(input("Enter first number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter Second number: "))

match op :
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Division by zero is not allowed")
    case _:
        print("Enter valid operator")
