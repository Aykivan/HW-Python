# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# a1 = int(input('Введите первый элемент: '))
# d = int(input('Введите разность(множитель): '))
# n = int(input('Введите количество эл-тов: '))

# for i in range(1, n + 1):
#     print(a1 + (i - 1) * d)

# Взял диапозон от 1 до n + 1, так как иначе он начинает считать с 0, и тогда вывод будет 5 7 9 11 13, а не 7 9 11 13 15
# хотя в эталонном решении написано просто range(n)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

maxx = int(input('Введите максимум: '))
minn = int(input('Введите минимум: '))
n = 10

some_list = [(random.randint(-10, 10)) for _ in range(n)]
print(some_list)

# Чтобы было поинтреснее сделал генерацию рандомного массива

for i in range(len(some_list)):
    if minn <= some_list[i] <= maxx:
        print(i)












