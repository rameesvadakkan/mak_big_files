import re

text = "My ID is A123B456"

digits = re.findall(r"\d", text)

print(digits)
