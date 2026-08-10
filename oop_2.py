class BankAccount:
    def __init__(self, owner_name, phone_number, deposit=0):
        self.owner_name = owner_name
        self.phone_number = phone_number
        self.balance = deposit

    def show_info(self):
        print(f"""
        =========== BANK ACCOUNT ============

        NAME: {self.owner_name}
        Phone no: {self.phone_number}
        Balance: {self.balance}
        """)

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Rs. {amount} deposited successfully.")
        print(f"New balance: Rs. {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
            print(f"New balance: Rs. {self.balance}")
        else:
            print("Insufficient balance.")

                    # DISPLAY 


# Sachin = BankAccount("Sachin Nepal", 9765571151, 10000)

# Sachin.show_info()

# Sachin.deposit_money(5000)

# Sachin.withdraw(3000)

# Sachin.show_info()




