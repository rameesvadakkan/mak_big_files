with open("welcome.txt","x") as f :
    f.write("Welcome to Python")
with open("welcome.txt") as f :
    print(f.read())