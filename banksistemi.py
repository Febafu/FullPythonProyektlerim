class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Balance: {self.balance}")

def main():
    name = input("Enter your name: ")
    account = Account(name)
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display_balance()
        elif choice == 4:
            break

if __name__ == "__main__":
    main()
