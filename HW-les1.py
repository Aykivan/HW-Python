# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# a = int(input('Введите число: '))
# summa = 0
# while a % 10 > 0:
#     summa += int(a % 10) - если убрать тут явное преобразование в int, решение не получается, не понимаю почему так, ведь сумма будет 
#                            состоять из целых чисел а, почему он выводит дробное без int, после деления он автоматически переводит числа в float?
#     a = a / 10
# print(summa)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# summa = int(input('Введите количество журавликов: '))
# ser = int(summa / 6)
# pet = ser
# kat = ((pet + ser)) * 2
# print(f'Сергей - {ser}, Петя - {pet}, Катя - {kat}')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# a = input('Введите номер билета: ')
# if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
#     print('YES')
# else:
#     print('NO')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

# честно говоря нашел решение от этой задачи в интернете, сам не додумался
