list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
numbers = len(list_players)
midle_index = numbers // 2
team1 = list_players[:midle_index:]
team2 = list_players[midle_index:]
print(team1)
print(team2)