from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, name, account_no, balance):
        self.__name = name
        self.__account_no = account_no
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def _withdraw(self, amount):
        self.__balance -= amount
        print(f"amount withdrew, new balance: {self.get_balance()}")
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"amount deposited : {self.__balance} new balance:{self.__balance}")
        else:
            print("amount should be positive")
    
    @abstractmethod
    def account_type(self):
        pass

class Savings_account(Account):
    def __init__(self, name, account_no, balance, interest_rate):
        super().__init__(name, account_no, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"added interest : {interest}")
    
    def withdraw(self, amount):
        if amount > self.get_balance():
            print("insufficient")
        else:
            super()._withdraw(amount)
    
    def account_type(self):
        return "Savings account"

class Checkings_account(Account):
    def __init__(self, name, account_no, balance, draft_limit):
        super().__init__(name, account_no, balance)
        self.draft_limit = draft_limit
        
    def withdraw(self, amount):
        if amount > self.get_balance() + self.draft_limit:
            print("draft limit exceeded")
        else:
            if amount > self.get_balance():
                limit_used = amount - self.get_balance()
                self.draft_limit = self.draft_limit - limit_used
            super()._withdraw(amount)
    
    def account_type(self):
        return "Checkings Account"

p = Savings_account("john", 1, 100, 12)
print(p.get_balance())
p.add_interest()
p.withdraw(20)
q = Checkings_account("doe", 2, 1000, 300)
print(q.get_balance())
q.withdraw(1200)

            