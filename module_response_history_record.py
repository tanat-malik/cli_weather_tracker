"""Записать историю запросов."""
import json
import datetime


def history_record(json_data):
    """Сохранение истории запроса."""
    city_name = json_data['name']
    country_name = json_data['sys']['country']
    city_coords = json_data['coord']
    temp = json_data['main']['temp']
    weather_desc = json_data['weather'][0]['description']
    response_status = json_data['cod']
    current_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')

    history_list = {
        'Статус запроса': response_status,
        'Город': city_name,
        'Страна': country_name,
        'Координаты': city_coords,
        'Температура': temp,
        'Описание погоды': weather_desc,
        'Время запроса': current_time
    }

    # Открываем файл response_history_record.json для чтения, и если там есть данные сохраняем их
    try:
        with open('response_history_record.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception:
        data = []  # если файл не существует или пустой

    # Добавляем новые данные
    data.append(history_list)

    # Сохраняем обратно
    with open('response_history_record.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
