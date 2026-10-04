class Account:
    def __init__(self, pin):
        self.pin = pin

    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4 and str(new_pin).isdigit():
            self.pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. Please enter a 4-digit numeric PIN.")
    def __str__(self):
        return f"Account PIN: {self.pin}"
account = Account(7474)
print(account)
account.set_pin()
