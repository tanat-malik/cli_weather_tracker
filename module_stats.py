"""Вывод статистики по погоде."""
import requests
import json

# НА ЗАМЕТКУ!!! СДЕЛАТЬ ВЫВОД ТАБЛИЦЕЙ


def get_stats(number):
    """Запрашиваем статистику за выбранный период."""
    try:
        # Для вывода статистики программа выбирает последний запрос(город)
        # из json-файла response_history_record.json
        with open('response_history_record.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            last_city_data = data[-1]['Город']
            lot = data[-1]['Координаты']['lon']
            lat = data[-1]['Координаты']['lat']

        url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lot}&daily=temperature_2m_max,temperature_2m_min&forecast_days={number}'
        response = requests.get(url=url)
        json_data = response.json()

        times = json_data['daily']['time']
        max_temps = json_data['daily']['temperature_2m_max']
        min_temps = json_data['daily']['temperature_2m_min']
        weather_dict = {}

        for counter, time in enumerate(times):
            weather_dict[time] = {
                'Макс темп': int(max_temps[counter]),
                'Мин темп': int(min_temps[counter]),
                'Средняя темп': int((max_temps[counter] + min_temps[counter]) / 2)
            }

        current_period = f'{number} день'
        if number > 1:
            current_period = f'{number} дней'

        print(f'Город {last_city_data}. Данные по погоде на {current_period}:')
        for item in weather_dict:
            print(item, weather_dict[item])
    except Exception:
        print('Файл для запроса статистики не найден')


def get_period(period):
    """Функция для выбора периода."""
    if period == 'day':
        get_stats(1)
    elif period == 'week':
        get_stats(7)
    elif period == 'weeks':
        get_stats(14)
