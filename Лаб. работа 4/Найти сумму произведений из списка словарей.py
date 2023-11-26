import json


def task() -> float:
    # Чтение JSON файла
    with open('input.json') as f:
        data = json.load(f)

    # Инициализация счетчика суммы произведений
    total = 0.0

    # Обход всех словарей
    for item in data:
        # Получение значения ключа "score"
        score = item.get('score')

        # Получение значения ключа "weight"
        weight = item.get('weight')

        # Вычисление произведения
        product = score * weight

        # Добавление произведения к общей сумме
        total += product

    # Округление результата до 3 знаков после запятой
    result = round(total, 3)

    return result


print(task())
