# Вопросы для группы "Компьютерное зрение"
# В текстовом файле data.txt записаны натуральные числа в виде квадратной матрицы. Числа в строке записаны через пробел.
# На языке python напишите программу, которая:
# 1. Считывает данные из файла data.txt, расположенного в одной директории с файлом программы.
# 2. Определяет и выводит на экран:
# a. Размер матрицы (например, если размер матрицы 3 х 3, то вывести нужно число 3).
# b. Количество четных чисел в матрице.
# c. Список чисел, кратных 3.
# d. Сумму чисел первого столбца матрицы.
#
# Пример файла data.txt:
# 3 45 67 3
# 45 66 7 90
# 2 6 34 100
# 50 21 24 30
#
# Прикрепите 2 файла:
#
# Файл программы с расширением py.
# Скриншот экрана, на котором видно файл data.txt, код программы и результат выполнения программы.

f = open('data.txt', 'r')

data = []
matrixSize = 0
countPositiveNumbers = 0
arrayNumbers3 = []
sumColl1 = 0

# for line in f:
#     data.append([int(x) for x in line.split()])
# matrixSize = len(data)
#
# for row in data:
#     for index, j in enumerate(row):
#         if index == 0:
#             sumColl1 += j
#         if j % 2 == 0:
#             countPositiveNumbers += 1
#         if j % 3 == 0:
#             arrayNumbers3.append(j)

for line in f:
    arrayStr = line.split(' ')
    matrixSize += 1

    for index, j in enumerate(arrayStr):
        j = int(j)
        if index == 0:
            sumColl1 += j

        if j % 2 == 0:
            countPositiveNumbers += 1

        if j % 3 == 0:
            arrayNumbers3.append(j)

print('Размер матрицы:', matrixSize)
print('Количество четных чисел в матрице:', countPositiveNumbers)
print('Список чисел, кратных 3:', arrayNumbers3)
print('Сумму чисел первого столбца матрицы:', sumColl1)
