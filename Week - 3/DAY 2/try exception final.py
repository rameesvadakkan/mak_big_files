try :
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 =num1/num2
    print(num3)
except ValueError:
    print("Error:could not convert string to Float")
except ZeroDivisionError:
    print("Error:Division by zero is not allowed")
except Exception as e:
    print("unexpected error:",e)

finally:
    print("Program completed")

