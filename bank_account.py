class BankAccount:
    def __init__(self, acc_num, holder, balance):
        self.__account_number = acc_num   # private
        self.__account_holder = holder
        self.__balance = balance
        self.transactions = []

    # Read-only account number
    @property
    def account_number(self):
        return self.__account_number

    # Balance getter
    @property
    def balance(self):
        return self.__balance

    # Balance setter with validation
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"Deposited {amount}")
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    # Withdraw
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print("Withdrawal successful")
        else:
            print("Insufficient funds")

    # Display info
    def display_account_info(self):
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__account_holder)
        print("Balance:", self.__balance)

    # Transaction history (BONUS)
    def show_transactions(self):
        print("Transaction History:")
        for t in self.transactions:
            print(t)


# BONUS: Subclass with interest
class SavingsAccount(BankAccount):
    def __init__(self, acc_num, holder, balance, interest_rate):
        super().__init__(acc_num, holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print("Interest added:", interest)


# Demonstration
acc1 = SavingsAccount("58111", "Shekinah", 1000, 0.05)

acc1.deposit(500)
acc1.withdraw(200)
acc1.add_interest()

acc1.display_account_info()
acc1.show_transactions()
