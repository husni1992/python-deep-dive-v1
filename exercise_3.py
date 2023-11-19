# List
# lists in python are also objects
names = ["Husny", "Zainab", "Fazana", "Shifna", "Gazzali"]
names[0] = "Huzny"
print(names[-1])  # prints last item in list, only seen in Python
print(names)
print(names[1:3])

# methods in lists
names.insert(0, "Ahamed")
names.append("Foobar")
print(names)
print(len(names));