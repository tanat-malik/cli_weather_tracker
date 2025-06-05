"""Чтение истории запросов."""
import json


def get_response_history():
    """Чтение файла история запросов."""
    try:
        with open('response_history_record.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print('История запросов\n')
            for counter, history in enumerate(data):
                print(f'Запрос #{counter + 1}:')
                print(f'Город: {history['Город']}')
                print(f'Температура: {history['Температура']}')
                print(f'Время запроса: {history['Время запроса']}')
                print()
    except Exception:
        print('История запросов отсутствует!')
