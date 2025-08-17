import re

txt = "who are you"
x = re.search("^are.*you$",txt)
if x :
    print("Yes")
else :
    print("No")    