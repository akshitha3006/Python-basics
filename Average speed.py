# these are the speeds of three cyclists
cyclist1 =int(input("Enter the speed of the first cyclist:"))
cyclist2 =int(input("Enter the speed of the second cyclist:"))
cyclist3 =int(input("Enter the speed of the third cyclist:"))
average_speed = (cyclist1 + cyclist2 + cyclist3)/3
print("The avaerage speed is :",average_speed)
if cyclist1 < average_speed:
    print("Cyclist1 is riding slower than the average speed")
elif cyclist2 < average_speed:
    print("Cyclist2 is riding slower than the average speed")
else:
    print("Cyclist3 is riding slower than the average speed")        