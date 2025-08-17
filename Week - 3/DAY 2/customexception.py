while True :
 try:
    age = int(input("Enter your Age: "))
    if age <= 18:
        raise ValueError("Age must be 18 or Greater.Now your not Eligible,Enter next person age")

    else:
        print("Your are eligible")
        break
 except ValueError as e:
    print(f"Error:{e}")

 except Exception as d :
    print(str(d))
 finally:
    print("Program Completed")