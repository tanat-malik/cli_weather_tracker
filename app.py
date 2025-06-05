"""Основной файл."""
import os
import argparse

from module_constants import BASE_URL, API_KEY
from module_response_weather import enter_data
from module_response_weather import render_weather_on_console
from module_response_history_record import history_record
from module_get_response_history import get_response_history
from module_stats import get_period
from module_units import change_units


def main():
    """Основная функция."""
    if os.name == 'nt':
        os.system('')  # Включает поддержку ANSI в консоли Windows
        os.system('cls' if os.name == 'nt' else 'clear')  # Windows: 'cls', Linux/macOS: 'clear'

    # Создание именованных опции
    parser = argparse.ArgumentParser()

    # Вводить латиницей(На будущее написать код на проверку ввода латиницей)
    parser.add_argument('-city', help='Получение информации о погоде по названию города', type=str)
    parser.add_argument('--coords', nargs=2, help='Широта и долгота через пробел', type=float)
    parser.add_argument('-history', action='store_true', help='Показать историю поиска')
    parser.add_argument('-stats', '--period', choices=['day', 'week', 'weeks'],
                        help='Просмотр статистики погоды за определенный период')
    parser.add_argument('-units', choices=['metric', 'imperial'], help='Изменение единицы измерения температуры')
    args = parser.parse_args()

    if args.city:  # Если ввели название города
        json_data = enter_data(BASE_URL, args.city, API_KEY)
        render_weather_on_console(json_data)
        history_record(json_data)
    elif args.coords:  # Если ввели координаты
        json_data = enter_data(BASE_URL, args.coords, API_KEY)
        render_weather_on_console(json_data)
        history_record(json_data)

    # Если запросили историю запросов
    if args.history:
        get_response_history()

    # Если запросили статистику
    if args.period:
        get_period(args.period)

    # Если выбрали опцию единицы измерения
    if args.units:
        change_units(args.units)


if __name__ == '__main__':
    main()
