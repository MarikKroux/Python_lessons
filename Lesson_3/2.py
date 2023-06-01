# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
# Возвращает случайное число в пределах заданного промежутка

count = int(input("Введите количество элементов: "))
n = int(input("Введите максимальное генерируемое число: "))
list_numbers = [randint(1, n) for i in range(count)]
print(list_numbers)

number = int(input("Введите число, близкое которому необходимо найти: ")) 
close_number = list_numbers[0]

for i in list_numbers:
    if abs(number - i) < abs(number - close_number):
        close_number = i

print(f"Самый близкий по величине элемент: {close_number}")