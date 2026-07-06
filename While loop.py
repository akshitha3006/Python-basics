number = int(input("Enter you number:"))
count=0
while number>0:
    number = number//10
    count = count +1
print("Total number of digits:",count)    