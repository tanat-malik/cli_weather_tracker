"""Библиотеки."""
import requests
import os
import argparse
import pyfiglet
from simple_chalk import chalk

from module_constants import BASE_URL
from module_constants import API_KEY
from module_constants import WEATHER_ICONS

if os.name == 'nt':
    os.system('')  # Включает поддержку ANSI в консоли Windows
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows: 'cls', Linux/macOS: 'clear'

parser = argparse.ArgumentParser()
parser.add_argument('-city', help='Получение информации о погоде по названию города')  # Создаем аргумент -city
parser.add_argument('--coords', nargs=2, help='Введите долготу и широту через пробел')  # Создаем аргумент --coords
args = parser.parse_args()
json_data = None


def enter_city(city):
    """Запрос по названию города."""
    global json_data
    print(chalk.yellow('Запрос по названию города'))
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url=url)
    json_data = response.json()


def enter_coords(coords):
    """Запрос по координатам."""
    global json_data
    print(chalk.yellow('Запрос по координатам'))
    lat, lon = coords
    url = f'{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    response = requests.get(url=url)
    json_data = response.json()


if isinstance(args.city, str):  # Если ввели название города
    enter_city(args.city)
elif isinstance(args.coords, list):  # Если ввели координаты
    enter_coords(args.coords)


# Сохраняем нужные даные для вывода на консоли
city_name = json_data['name']
country_name = json_data['sys']['country']
current_temp = json_data['main']['temp']
temp_feels_like = json_data['main']['feels_like']
weather_desc = json_data['weather'][0]['description']
weather_icon = WEATHER_ICONS[json_data['weather'][0]['icon']]

render_weather = f'{pyfiglet.figlet_format(city_name)}\n'
render_weather += f'City: "{city_name}" Country: {country_name}\n'
render_weather += f'{weather_desc} {weather_icon} \n'
render_weather += f'Temperature: {current_temp:.0f}°C\n'
render_weather += f'Feels like: {temp_feels_like:.0f}°C\n'

print(chalk.green(render_weather))  # Вывод на консоль
