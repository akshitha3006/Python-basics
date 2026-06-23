medical_cause = input("Enter the medical cause in Y for yes and N for no:")
attendance = int(input("Enter the attendance percentage:"))
if medical_cause == "Y":
     print("The student is eligible to write the exam")
else:  
     if attendance>75:
          print("The student is allowed to write the exam") 
     else:
          print("The student is not allowed to write the exam")      