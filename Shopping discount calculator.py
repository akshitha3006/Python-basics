while True:
    try:
        bill = float(input("Enter shopping bill amount: "))

        if bill < 0:
            raise ValueError("Bill amount cannot be negative.")
    except ValueError as e:
        print("Invalid input. Please enter a valid number.")
        continue
    else:
        discount = bill*0.10
        final_price=bill-discount
        print("The discount amount is:", discount)
        print("The final price after discount is:", final_price)
        break
    finally:
        print("Thank you for using the shopping discount calculator.")    