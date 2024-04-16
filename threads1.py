import threading
import time

# печатаем числа
def print_numbers():
    for i in range(1, 11):
        print(i, flush=True)
        time.sleep(1)

# печатаем буквы
def print_letters():
    for char in range(ord('a'), ord('k')):
        print(chr(char), flush=True)
        time.sleep(1)

# Запускаем потоки
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
# Ждем пока закончат
thread1.join()
thread2.join()
