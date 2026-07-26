def calculate_bill(price,quantity):
    total = price * quantity
    return total

item_name = input("Enter the item name: ")
item_price = float(input("Enter the item price: "))
item_quantity = int(input("Enter the item quantity: "))
final_price = calculate_bill(item_price, item_quantity)
print("------ART SUPPLIES BILL------")
print("Item Name:", item_name)
print("Item Price: $", item_price)
print("Item Quantity:", item_quantity)
print("Total Price: $", final_price)
                   