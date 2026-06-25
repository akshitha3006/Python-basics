name = "Akshitha"
length= len(name)

reverse = ""
for i in range(length-1,-1,-1):
    reverse += name[i]
print("The reverse of the given string is",reverse)
