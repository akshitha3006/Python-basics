try:
    num1,num2=eval(input("Enter two numbers separated by a comma: "))
    
    result=num1/num2
    print("the result is:",result)
except ZeroDivisionError:  
    print("Division by zero is error!")  
except SyntaxError:
    print("Comma is missing, please enter two numbers separated by a comma")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will work no matter what")    
 

