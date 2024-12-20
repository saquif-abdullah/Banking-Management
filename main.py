class BankAccount:
    def __init__(self, holder_name="Default User", initial_balance=0.0):
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print(f"Successfully deposited {amount:.2f}. Updated balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance for the withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount:.2f}. Updated balance: {self.balance:.2f}")

    def get_balance(self):
        print(f"Current balance: {self.balance:.2f}")

def main():
    default_user = input("Enter Default User : ")
    balance = float(input("Enter Initial Balance : "))
    account = BankAccount(default_user, balance)

    while True:
        print("\n--- Banking Management System ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")

        choice = input("Choose an option : ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.get_balance()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
