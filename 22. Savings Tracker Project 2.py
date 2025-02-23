import random

# Global variable to store all created accounts
account_list = []
routing_number = 234543345

# Utility Functions
def account_switcher(choice):
    return {1: "Checking", 2: "Savings", 3: "Business"}.get(choice)

def find_account_by_number(number):
    for account in account_list:
        if account.get_number() == number:
            return account
    return None

# Classes
class Bank:
    def __init__(self, first, last, money, account_type):
        self.first = first
        self.last = last
        self.money = money
        self.routing_number = routing_number
        self.number = int(random.random() * 1000000000000)
        self.account_type = account_type

    def set_amount(self, amount):
        self.money = amount

    def get_balance(self):
        return self.money

    def get_number(self):
        return self.number

    def get_customer(self):
        return self.first, self.last

    def get_type(self):
        return self.account_type

    def withdraw(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f"Withdrawn {amount}. New balance: {self.money}")
        else:
            print("Insufficient funds. Your balance is only $", self.money)

    def deposit(self, amount):
        self.money += amount
        print(f"Deposited {amount}. New balance: {self.money}")

    def transfer(self, to_account, amount):
        if self.money >= amount:
            self.money -= amount
            to_account.deposit(amount)
            print(f"Transferred {amount} from {self.account_type} to {to_account.get_type()}.")
        else:
            print("Insufficient funds for transfer.")

# Main Functions
def create_account(first, last, money, account_type):
    for account in account_list:
        if account.get_type() == account_type and (account.first == first and account.last == last):
            print(f"You already have a {account_type} account.")
            return

    new_account = Bank(first, last, money, account_type)
    account_list.append(new_account)
    print(f'Your {account_type} account has been created successfully with name: {new_account.first} {new_account.last}, '
          f'account number {new_account.get_number()} and routing number {new_account.routing_number}.')
    return new_account

def view_balance():
    if len(account_list) == 0:
        print("You have no accounts.")
        return

    print("Which account balance do you want to view?")
    for i, account in enumerate(account_list, 1):
        print(f"{i}. {account.get_type()} account with balance ${account.get_balance()}")

def withdraw():
    if len(account_list) == 0:
        print("You have no accounts.")
        return

    account_num = int(input("Enter the account number to withdraw from: "))
    account = find_account_by_number(account_num)
    if account:
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    else:
        print("Invalid account number.")

def transfer():
    if len(account_list) < 2:
        print("You need at least two accounts to make a transfer.")
        return

    from_account_num = int(input("Enter the account number to transfer from: "))
    to_account_num = int(input("Enter the account number to transfer to: "))

    from_account = find_account_by_number(from_account_num)
    to_account = find_account_by_number(to_account_num)

    if from_account and to_account:
        amount = float(input("Enter the amount to transfer: "))
        from_account.transfer(to_account, amount)
    else:
        print("One or both account numbers are invalid.")

def main():
    print("Welcome to Hatter Bank!")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    while True:
        try:
            initial_deposit = float(input("How much money would you like to deposit to start your account? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            account_type_choice = int(input("Select account type: 1. Checking 2. Savings 3. Business: "))
            if account_type_choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Try again.")
            break
        except ValueError as e:
            print(e)

    # Account type is assigned after validation
    account_type = account_switcher(account_type_choice)
    create_account(first_name, last_name, initial_deposit, account_type)

    while True:
        print("\nWhat would you like to do next?")
        print("1. Create another account")
        print("2. View Balance")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. Quit")

        try:
            action = int(input("Choose an option (1-5): "))
            if action == 1:
                account_type_choice = int(input("Select account type: 1. Checking 2. Savings 3. Business: "))
                if account_type_choice not in [1, 2, 3]:
                    print("Invalid account type choice.")
                    continue
                deposit = float(input("How much would you like to deposit? "))
                account_type = account_switcher(account_type_choice)
                create_account(first_name, last_name, deposit, account_type)
            elif action == 2:
                view_balance()
            elif action == 3:
                withdraw()
            elif action == 4:
                transfer()
            elif action == 5:
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the main program
if __name__ == "__main__":
    main()
