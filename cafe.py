import threading
import time
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables

    def customer_arrival(self):
        customer_number = 0
        while customer_number < 20:  # количество посетителей
            customer_number += 1
            customer = Customer(customer_number, self)
            customer.start()
            time.sleep(1)  # Интервал прибытия посетителей

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                time.sleep(5)  # Время обслуживания
                table.is_busy = False
                customer.leave()
                break
        else:
            print(f"Посетитель номер {customer.number} ожидает свободный стол.")
            self.queue.append(customer)

class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        print(f"Посетитель номер {self.number} прибыл.")
        self.cafe.serve_customer(self)

    def leave(self):
        print(f"Посетитель номер {self.number} покушал и ушёл.")

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()