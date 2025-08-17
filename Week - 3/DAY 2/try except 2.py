while True :
  try:
   num = input("Enter a number: ")
   string1 = int(num)
   print("Conversion successful. The number is:",num)
   continue
  except ValueError:
    print("Error: Input is not a valid integer. Try again")
  finally:
    print("End of program")