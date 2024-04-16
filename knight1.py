import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.days += 1
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
            self.enemies -= self.skill
            time.sleep(1)  # Имитация дня битвы

        print(f"{self.name} одержал победу спустя {self.days} дней!")


# Создаем рыцарей
knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения

# Запускаем битву
knight1.start()
knight2.start()

# Ждем завершения битвы
knight1.join()
knight2.join()

print("Все битвы закончились!")