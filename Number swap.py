num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
print("Before swapping: num1=",num1," num2=",num2," num3=",num3)
temporary=num1
num1 = num2
num2 = num3
num3 = temporary
print("After swapping: num1=",num1," num2=",num2," num3=",num3)
