person = {
    "name":"ramees",
    "age" : 30,
    "city" : "kottakkal"
}

print(person)

print(person["name"])

x = person.get("age")
print(x)

y = person.keys()
print(y)

person["age"] = 32

print(person)

print(person.values())

print(person.pop("age"))
print(person)

for y in person.values():
    print(y)
