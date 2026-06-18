sub1 = int(input("Enter the marks of subject 1:" ))
sub2 = int(input("Enter the marks of subject 2:" ))
sub3 = int(input("Enter the marks of subject 3:" ))
sub4 = int(input("Enter the marks of subject 4:" ))
sub5 = int(input("Enter the marks of subject 5:" ))
average = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
if average in range (91,101):
    print("Your grade is A")
elif average in range (81,91):
    print("Your grade is B")
elif average in range (71,81):
    print("Your grade is C")
elif average in range (61,71):
    print("Your grade is D")
else:
    print("Your grade is F")               