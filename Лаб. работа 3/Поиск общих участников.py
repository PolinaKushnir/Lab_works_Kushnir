# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter=","):
    first_group = participants_first_group.split(delimiter)
    second_group = participants_second_group.split(delimiter)
    common_participants = sorted(list(set(first_group) & set(second_group)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
