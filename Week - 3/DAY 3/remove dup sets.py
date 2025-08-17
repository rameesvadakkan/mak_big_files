while True :
 try :
    value = input("Enter number: ").split()
    myset = set(value)
    print(myset)
    break
 except Exception as e :
     print(str(e))
 except:
     print("Error!")
 finally:
    print("End of program")