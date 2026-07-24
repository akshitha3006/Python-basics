def total_calc(bill_amount,tip_perc):
    tip_amount = bill_amount * (tip_perc/ 100)
    print("Subtotal amount:", bill_amount)
    print("Tip amount:", tip_amount)
    total_amount = bill_amount + tip_amount
    print("Total amount:", total_amount)
    return total_amount
total_bill = total_calc(100, 15)