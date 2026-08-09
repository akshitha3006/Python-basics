print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Enter your choice (1-4): "))
if operation==1:
    print("You have selected Addition.")
    try:
       def calculate_addition(num1,num2):
         return num1+num2
       num1=float(input("Enter the first number: "))
       num2=float(input("Enter the second number: "))
       result=calculate_addition(num1,num2)
       print("The result of addition of given two numbers is:", result)
    except ValueError:
       print("Invalid input. Please enter a Valid Number")   
       
elif operation==2:
    print("You have selected Subtraction.")
    try:
       def calculate_subraction(num1,num2):
         return num1-num2
       num1=float(input("Enter the first number: "))
       num2=float(input("Enter the second number: "))
       result=calculate_subraction(num1,num2)
       print("The result of subtraction of given two numbers is:", result)
    except ValueError:
       print("Invalid input. Please enter a VAlid Number")
elif operation==3:
    print("You have selected Multiplication.")
    try:
      def calculate_multiplication(num1,num2):
         return num1*num2
      num1=float(input("Enter the first number: "))
      num2=float(input("Enter the second number: "))
      result=calculate_multiplication(num1,num2)
      print("The result of multiplication of given two numbers is:", result)
    except ValueError:
          print("Invalid input. Please enter a Valid Number")
    
elif operation==4:
    print("You have selected Division.")
    try: 
        def calculate_division(num1,num2):
            return num1/num2
        num1=float(input("Enter the first number: "))  
        num2=float(input("Enter the second number: "))
        result = calculate_division(num1,num2)
        print("The result of division of given two numbers is:", result)
    except ValueError:
        print("Invalid input. Please enter a Valid Number")
    except ZeroDivisionError:
           print("Division by zero is not defined. Please enter a valid number.")
else:
    print("Invalid choice. Please select a Valid Operation from 1-4.")


    

 