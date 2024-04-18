import threading

class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()  # Создаем блокировку

    def deposit(self, amount):
        with self.lock:  #  блокировка
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.lock:  #блокировка
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print("Not enough money")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(11):
        account.withdraw(amount)

account = BankAccount()  # Создаем экземпляр банковского счета

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()