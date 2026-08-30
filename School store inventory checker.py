items = ["Pencil","Pen","Eraser","Ruler","Notebooks"]
stock_count=[10,29,36,0,7]
paired = list(zip(items,stock_count))


inventory = {item:count for item, count in paired}
print("Full Inventory:",inventory)

in_stock_items = [item for item in items if inventory[item]>0]
print("Items in stock:",in_stock_items)

chosen_items = input("Which item do you want to purchse? ")
if chosen_items not in inventory or inventory[chosen_items]==0:
    print(chosen_items,"is out of stock! Stopping the checker.")
    exit()

prices = [10,30,6,45,36] 
markup = int(input("Enter the markup amount to add to every price: "))
marked_up_prices = list(map(lambda p: p+markup,prices)) 
print("Marked Up Prices:",marked_up_prices)

item_index= items.index(chosen_items)
chosen_price = marked_up_prices[item_index]
print("Price of",chosen_items,"After markup:",chosen_price)

inventory[chosen_items]= inventory[chosen_items]-1
print(chosen_items,"purchsed! Remaining stock:",inventory[chosen_items])

print("====== SCHOOL STOCK INVENTORY CHECKER ======")
print("Item bought:",chosen_items)
print("Price paid:",chosen_price)
print("Updated inventory:",inventory)
print("=============================================")

