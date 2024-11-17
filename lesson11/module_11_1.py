# Задача:
# Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
# После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями.
# К каждой библиотеке дана ссылка на документацию ниже.
# Если вы выбрали:
# requests - запросить данные с сайта и вывести их в консоль.
# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
# В приложении к ссылке на GitHub напишите комментарий о возможностях,
# которые предоставила вам выбранная библиотека и как вы расширили возможности Python с её помощью.
# Примечания:
# Можете выбрать не более 3-х библиотек для изучения.
# Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.

import numpy as np

# Создание одномерного массива:
array1 = np.array([1, 2, 3, 4, 5])
print("Одномерный массив:", array1)

# Векторные операции (умножение на скаляр):
array2 = array1 * 2
print("Умножение на 2:", array2)

# Создание двумерного массива и вычисление суммы:
array3 = np.array([[1, 2, 3], [4, 5, 6]])
total_sum = np.sum(array3)
print("Сумма элементов двумерного массива:", total_sum)

# Вычесление среднего и стандартного отклонения:
mean_value = np.mean(array1)
std_deviation = np.std(array1)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_deviation)


# визуализация данных, создание графиков, настройка оформления графиков.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title('Простой график')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Добавление легенды на график:
plt.plot(x, y, label='Линия 1')
plt.plot(x, [i ** 2 for i in x], label='Линия 2')
plt.legend()
plt.show()

# Создание круговой диаграммы:
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Круговая диаграмма')
plt.show()

import requests

# Работа с параметрами в URL:
params = {'q': 'requests+language:python'}
response = requests.get('https://api.github.com/search/repositories', params=params)
print(response.json())

# Добавление заголовков к запросу:
headers = {'User-Agent': 'my-app'}
response = requests.get('https://api.github.com/user', headers=headers)
print(response.json())

# Отправка POST-запроса:
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())