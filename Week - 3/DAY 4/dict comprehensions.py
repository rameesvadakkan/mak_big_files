people = {'Ramees': 32,"Arun":29,'John':35}
upper_dict = {k.upper():v for (k,v) in people.items()}
print(upper_dict)
name_upper = {k:k.upper() for k in people.keys()}
print(name_upper)