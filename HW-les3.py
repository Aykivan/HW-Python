# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# n = int(input('Введите длину массива: '))
# array = []
# for el in range(n):
#     array.append(el)
# print(array)
# # по условию задачи х = 3
# x = 3
# # x = int(input('Введите исокомое число: '))
# count = 0
# for i in array:
#     if array[i] == x:
#         count += 1
# print(f'Элементы х = {x} встречается в массиве {count} раз')
        
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# for i in array:
#     raz = x - array[i]
#     if raz < x - isk:
#         isk = raz
# print(f'Ближайшее значение к числу x будет равно {isk}')

# n = int(input('Введите длину массива: '))
# array = []
# for el in range(n):
#     array.append(el + 1)
# array = list(array)
# print(array, type(array))

# x = 6
# minraz = (x - array[0])**2 # Минимальная разница по модулю (для сравнения первый элемент)
# b = 0 # Нулевой индекс a[i]

# # for i in array: - если использую данную конструкцию выдает ошику, при этом, если во время формирования массива в строке array.append(el + 1) убрать + 1, то тогда 
# # никакой ошибки нет и циккл for i in array работает нормально, было бы здорово узнать почему
# i = 0
# while i < len(array):
#     if (x-array[i])**2 <= minraz:
#         minraz = (x-array[i])**2
#         b = i
#     i += 1
# print('Самое близкое значение элемента массива: ', array[b])

#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.



# word = input('Введите слово: ')
# for i in word:
#     print(word(i))

# import re
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# text = input().upper()
# if isCyrillic(text):
# 	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in points_en.items() if i in v]))

# Все это решение взято из гугла, понять это самому мне не удалось, очень тяжелая для меня тема, много всего чего мы не изучали не на семинаре не где либо еще
# жду разбора этого дз, тк как в 4 семинаре его не было.

#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------