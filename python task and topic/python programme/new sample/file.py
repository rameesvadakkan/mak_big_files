

# Write to mylife3.txt
with open("mylife3.txt", "w") as file2:
    file2.write("hai ramees vadakkan")

# Read from mylife3.txt
with open("mylife3.txt", "r") as file2:
    content = file2.read(6)
    print(content)
