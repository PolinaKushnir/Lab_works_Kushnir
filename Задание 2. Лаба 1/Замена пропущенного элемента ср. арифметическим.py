numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_1 = sum(numbers[:4])
sum_2 = sum(numbers[5:])
sum_12 = sum_1 + sum_2
count = len(numbers)
sr_arifm = sum_12 / count
numbers[4] = sr_arifm
print("Измененный список:", numbers)
