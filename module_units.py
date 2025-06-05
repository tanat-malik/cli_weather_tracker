"""Функции для работы с единицей измерения."""


def change_units(unit):
    """Изменение единицы измерения."""
    # С помощью этой функции, пользователь может поменять единицу измерения
    # try:
    #     with open('temp_unit.txt', 'w', encoding='utf-8') as file:
    #         file.write(unit)
    #         print('Единица измерения успешно изменена!')
    # except Exception as ex:
    #     print(f'Ошибка! {ex}')

    try:
        with open('temp_unit.txt', 'r+', encoding='utf-8') as file:
            file.seek(0)  # вернуться в начало файла
            file.write(unit)  # записать новое значение
            file.truncate()  # удалить все что осталось после новой записи
            print('Единица измерения успешно изменена!')
    except FileNotFoundError:  # Если файла не существует
        with open('temp_unit.txt', 'w', encoding='utf-8') as file:
            file.write(unit)
            print('Единица измерения успешно изменена!')
    except Exception as ex:
        print(f'Ошибка! {ex}')


def get_temp_unit():
    """Извлекаем значение для дальнейшей работы."""
    # Используем ее для добавления в url, или в какую-либо переменную с температурой
    temp_unit = ''
    try:
        with open('temp_unit.txt', 'r', encoding='utf-8') as file:
            temp_unit = file.read()
    except Exception:
        print('Ошибка!')
    return temp_unit
