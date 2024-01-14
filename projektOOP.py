import random

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposit of {amount}$")
            print(f"Deposit of {amount}$ successful. New balance: {self.__balance}$")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawal of {amount}$")
            print(f"Withdrawal of {amount}$ successful. New balance: {self.__balance}$")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    def display_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: {self.__balance}$")
        print("Transaction History:")
        for transaction in self.__transactions:
            print(f"- {transaction}")

    @staticmethod
    def generate_account_number():
        # Generate a random 9-digit account number
        return ''.join(random.choice('0123456789') for _ in range(9))

# Example usage of the BankAccount class
account_number = BankAccount.generate_account_number()
account1 = BankAccount(account_number=account_number, account_holder="John Doe", balance=1000)

account1.deposit(500)
account1.withdraw(200)
account1.display_info()
