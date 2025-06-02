"""Библиотеки."""
import os
import argparse

from module_constants import BASE_URL
from module_constants import API_KEY

from module_response_weather import enter_city
from module_response_weather import enter_coords
from module_response_weather import render_weather_on_console

from module_response_history_record import history_record
from module_get_response_history import get_response_history

if os.name == 'nt':
    os.system('')  # Включает поддержку ANSI в консоли Windows
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows: 'cls', Linux/macOS: 'clear'

# Создание именованных опции
parser = argparse.ArgumentParser()
parser.add_argument('-city', help='Получение информации о погоде по названию города', type=str)
parser.add_argument('--coords', nargs=2, help='Введите долготу и широту через пробел', type=float)
parser.add_argument('-history', action='store_true', help='Показать историю поиска')
args = parser.parse_args()

json_data = None
if isinstance(args.city, str):  # Если ввели название города
    json_data = enter_city(BASE_URL, args.city, API_KEY)
    render_weather_on_console(json_data)
    history_record(json_data)
elif isinstance(args.coords, list):  # Если ввели координаты
    json_data = enter_coords(BASE_URL, args.coords, API_KEY)
    render_weather_on_console(json_data)
    history_record(json_data)

# Если запросили историю запросов
if args.history:
    get_response_history()
