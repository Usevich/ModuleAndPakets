import threading

class WarehouseManager:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()  #создаем блокировку чтобы не допустить одновременное обращение к данным из разных потоков

    def process_request(self, request):
        product, action, amount = request
        with self.lock:  #используем блокировку
            if action == "receipt":
                if product in self.data:
                    self.data[product] += amount
                else:
                    self.data[product] = amount
            elif action == "shipment":
                if product in self.data and self.data[product] >= amount:
                    self.data[product] -= amount

    def run(self, requests):
        threads = []
        for req in requests:
            t = threading.Thread(target=self.process_request, args=(req,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
#Пример работы:
# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)