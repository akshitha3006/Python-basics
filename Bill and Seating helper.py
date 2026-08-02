def calculate_bill(food_amount,tax_percentage,tip_percentage):
    total = food_amount + (food_amount * tax_percentage/100)+(food_amount * tip_percentage / 100)
    return total 

def counting_seating_arrangements(n):
    """Calculates total possible seating arrangements for n guests using recursion"""
    if n == 0 or  n == 1:
        return 1
    return n * counting_seating_arrangements(n - 1)


food = 100
tax = 10
tip = 15
total_bill = calculate_bill(food,tax,tip)
print("Total Bill:",total_bill)
print("\nFunctionDocstring:")
print(counting_seating_arrangements.__doc__)
guests = 4
arrangements = counting_seating_arrangements(guests)
print("Total seating arrangements for",guests,"guests:",arrangements)
