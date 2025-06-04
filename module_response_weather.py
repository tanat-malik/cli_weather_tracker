"""Запрос данных по погоде."""
import requests
import pyfiglet
from simple_chalk import chalk
from module_constants import WEATHER_ICONS  # Иконки


def enter_city(url, city, key):
    """Запрос по названию города."""
    print(chalk.yellow('Запрос по названию города'))
    url = f'{url}?q={city}&appid={key}&units=metric'
    response = requests.get(url=url)
    return response.json()


def enter_coords(url, coords, key):
    """Запрос по координатам."""
    print(chalk.yellow('Запрос по координатам'))
    lat, lon = coords
    url = f'{url}?lat={lat}&lon={lon}&appid={key}&units=metric'
    response = requests.get(url=url)
    return response.json()


def render_weather_on_console(data):
    """Отрисовка данных на консоли."""
    city_name = data['name']
    country_name = data['sys']['country']
    current_temp = int(data['main']['temp'])
    temp_feels_like = data['main']['feels_like']
    weather_desc = data['weather'][0]['description']
    weather_icon = WEATHER_ICONS[data['weather'][0]['icon']]

    render_weather = f'{pyfiglet.figlet_format(city_name)}\n'
    render_weather += f'City: "{city_name}" Country: {country_name}\n'
    render_weather += f'{weather_desc} {weather_icon} \n'
    render_weather += f'Temperature: {current_temp:.0f}°C\n'
    render_weather += f'Feels like: {temp_feels_like:.0f}°C\n'

    print(chalk.green(render_weather))  # Вывод на консоль
