cost_price = int(input("Enter the cost of an orange:"))
selling_price = int(input("Enter the selling price of an orange:"))
if selling_price >cost_price:
    print("The profit amount is", selling_price - cost_price)
else:
    print("The loss amount is",cost_price - selling_price)    

