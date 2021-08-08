import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.opened = None
        self.lock = threading.Lock()

    def get_balance(self):
        if self.opened:
            return self.balance
        else:
            raise ValueError('You can\'t check the balance of a closed account.')

    def open(self):
        if self.opened is None:
            self.opened = True
        else:
            raise ValueError('You can\'t open an account that is already open.')

    def deposit(self, amount):
        if not self.opened:
            raise ValueError('You can\'t deposit money to a closed account.')
        
        if amount < 0:
            raise ValueError('You can\'t deposit a negative amount of money.')

        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.opened:
            raise ValueError('You can\'t withdraw money from a closed account.')

        if (self.balance - amount) < 0:
            raise ValueError('You can\'t withdraw more money than you have in your account.')
        else:
            with self.lock:
                self.balance -= amount
                
        if amount < 0:
            raise ValueError('You can\'t withdraw a negative amount of money.')
        
    def close(self):
        if self.opened:
            self.opened = None
            self.balance = 0
        else:
            raise ValueError('You can\'t close an account that is already closed.')