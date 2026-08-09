def calculate_change(amount_paid, ticket_cost):
    
    change = amount_paid - ticket_cost
    if change == 0:
        pass
    return change
ticket_cost = 10
total_amount_paid = 0
valid_coins = [ 1,2,5,10]
print("----Parking Ticket Payment Helper----")
print("Ticket cost is:", ticket_cost)
print("Valid coins are:", valid_coins)
while True:
    coin = int(input("Enter a coin (1, 2, 5,or 10) : "))
    if coin not in valid_coins:
        print("Invalid coin. Please enter a valid coin.")
        continue
    total_amount_paid += coin
    print("Total amount paid so far:", total_amount_paid)
    if total_amount_paid >= ticket_cost:
        break
change = calculate_change(total_amount_paid, ticket_cost)
print("\n----Payment Summary----")
print("Ticket cost:", ticket_cost)
print("Total amount paid:", total_amount_paid)
print("Change to be returned:", change)
print("Thank you for your payment. Have a great day!")