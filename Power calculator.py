base = int(input("Enter the base number:"))
exponent = int(input("Enter the exponent:"))
total = 1
for i in range(0,exponent):
    total = total * base
    print(total)