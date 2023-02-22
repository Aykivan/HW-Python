# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines 
# (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# num = int(input('Введите число: '))

# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as some_file:
#         text = some_file.read().splitlines()
#         for ind in range(1, lines + 1):
#             print(text[- ind])

# if num >= 1:
#     read_last(num, 'HW-les8.txt')
# else:
#     print('Введенное число не подходит.')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько)

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as some_file:
        words = some_file.read().split()
        maxx = 0
        word = ''
        for ind in range(len(words)):
            if maxx < len(words[ind]):
                maxx = len(words[ind])
        for ind in range(len(words)):
            if maxx == len(words[ind]):
                word = words[ind]
    return word
        
print(longest_words('HW-les8.txt'))
