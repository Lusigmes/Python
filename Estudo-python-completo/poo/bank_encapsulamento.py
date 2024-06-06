class Account:
    def __init__(self ,agency, balance=0):
        self.agency = agency
        self._balance = balance


    def deposit(self, balance):
        self._balance += balance

    def withdraw(self, balance):
        self._balance -= balance


    def get_balance(self):
        return self._balance

conta = Account("1234", 1.97)
conta.deposit(5)
print(conta.agency)
print(conta.get_balance())