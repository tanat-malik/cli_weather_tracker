"""Запрос данных по погоде."""
import requests
import pyfiglet
from simple_chalk import chalk
from module_constants import WEATHER_ICONS  # Иконки
from module_units import get_temp_unit

temp_unit = get_temp_unit()


def enter_data(url, data, key):
    """Запрос данных."""
    if isinstance(data, str):
        print(chalk.yellow('Запрос по названию города'))
        url = f'{url}?q={data}&appid={key}&units={temp_unit}'
    else:
        lat, lon = data
        print(chalk.yellow('Запрос по координатам'))
        url = f'{url}?lat={lat}&lon={lon}&appid={key}&units={temp_unit}'
        
    response = requests.get(url=url)
    return response.json()


def render_weather_on_console(data):
    """Отрисовка данных на консоли."""
    city_name = data['name']
    country_name = data['sys']['country']
    current_temp = str(int(data['main']['temp']))
    temp_feels_like = str(int(data['main']['feels_like']))
    weather_desc = data['weather'][0]['description']
    weather_icon = WEATHER_ICONS[data['weather'][0]['icon']]

    if temp_unit == 'metric':
        current_temp += '°C'
        temp_feels_like += '°C'
    else:
        current_temp += '℉'
        temp_feels_like += '℉'

    render_weather = f'{pyfiglet.figlet_format(city_name)}\n'
    render_weather += f'City: "{city_name}" Country: {country_name}\n'
    render_weather += f'{weather_desc} {weather_icon}\n'
    render_weather += f'Temperature: {current_temp}\n'
    render_weather += f'Feels like: {temp_feels_like}'

    print(chalk.green(render_weather))  # Вывод на консоль
