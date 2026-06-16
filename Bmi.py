weight = float(input("Enter your weight in kg:"))
height= float(input("Enter your height in meters:"))
bmi = weight/(height)**2
if bmi>=18.5 and bmi<=24.9:
    print("Your Bmi is",bmi,"and your healthy")
elif bmi<18.5:
    print("Your bmi is",bmi,"and you are underweight")
else:
    print("Your bmi is",bmi,"and you are overweight")    

