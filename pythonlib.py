import requests

print('============== requests ==============')
url = 'https://ya.ru'
response = requests.get(url)
if response.ok:
    print(response.text)
else:
    print('Ошибка при запросе:', response.status_code)


import pandas as pd
print('============== pandas ==============')
df = pd.read_csv('data.csv')
mean_value = df['x'].mean()
print('Среднее значение колоники X:', mean_value)
print('Среднее значение колоники Y:', df['y'].mean())
import numpy as np
print('============== numpy ==============')
array = np.array([1, 2, 3, 4, 5])
array_squared = np.square(array)
print('Квадраты чисел массива:', array_squared)
print('Числа умноженые на 10',np.multiply(array,10))

import matplotlib.pyplot as plt
print('============== matplotlib ==============')
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Для продолжения зкакрой меня')
plt.show()

from PIL import Image, ImageFilter
print('============== pillow ==============')
image = Image.open('image.jpg')
# Измените размер:
image_resized = image.resize((100, 100))

# Примените эффект размытия:
image_blurred = image.filter(ImageFilter.BLUR)

# Сохраните в другой формат:
print("Записываем изображение с новым размером")
image_resized.save('image_resized.png')
print("Записываем размытое изображение")
image_blurred.save('image_blurred.png')
