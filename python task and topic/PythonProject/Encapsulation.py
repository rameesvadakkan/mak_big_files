from time import sleep


class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposite(self,amount):
        if amount > 0:
            self.amount = amount
            self.__balance += amount
            print(f"Deposited {self.amount} Balance {self.__balance}")
        else:
            print("deposited amount not valid")
    def get_balance(self):
        return self.__balance
acc = BankAccount("Ramees",10000)
acc.deposite(1000)
print(acc.get_balance())