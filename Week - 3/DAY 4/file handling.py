try:
 with open('weekly.txt','r') as file_name : #read
  print(file_name.read())
  print("Read Successfully")
except Exception as e :
  print(str(e))

with open('weekly.txt','a') as file_name : #append
    print(file_name.write("\n"+"will start revision today"))

