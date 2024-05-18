# Получение и анализ данных о погоде
# Цель
# Целью задания является закрепление навыков работы с методом response.json()
# Условия
#     Используйте API погодного сервиса, расположенный по адресу:
#     Данный API возвращает погодные данные для заданного города в формате JSON.
# Задача
#     Напишите код, который осуществляет GET-запрос к указанному API для получения погодных данных заданного города.
#     Преобразовать полученный JSON-ответ в Python-объект с помощью метода response.json().
#     Проанализировать данные и определить дату с самой минимальной температурой.
# Результат
# Найдена дата с самой минимальной температурой. Формат даты должен быть таковым, как представлен в данных по ссылке API.
# Пример вывода:
# 2023-10-01

import requests

# URL погодного сервиса
URL = "https://parsinger.ru/3.4/1/json_weather.json"

# Выполнение GET-запроса
response = requests.get(URL)

# Проверка статуса ответа
if response.status_code != 200:
    print(f'Ошибка получения данных: {response.status_code}')
else:
    # Преобразование JSON-ответа в Python-объект
    weather_data = response.json()

    # Инициализация переменных для хранения минимальной температуры и соответствующей даты
    min_temp = "0"
    min_temp_date = None

    # Проход по всем записям и поиск минимальной температуры
    for record in weather_data:
        try:
            temp = int(record['Температура воздуха'].strip("°C"))
            date = record['Дата']
        except ValueError:
            print(f"Ошибка")
            continue
        else:
            if temp < int(min_temp):
                min_temp = temp
                min_temp_date = date
    # вывод даты и минимальной температуры
    print(min_temp_date, min_temp)
