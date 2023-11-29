import json


def task() -> float:
    # Чтение JSON файла
    with open('input.json') as f:
        data = json.load(f)

        total = sum(item.get('score') * item.get('weight') for item in data)

    # Округление результата до 3 знаков после запятой
    result = round(total, 3)

    return result

print(task())
