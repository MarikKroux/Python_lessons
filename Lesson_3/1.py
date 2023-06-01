# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
# Возвращает случайное число в пределах заданного промежутка

count = int(input("Введите количество элементов: "))
n = int(input("Введите максимальное генерируемое число: "))
list_numbers = [randint(1, n) for i in range(count)]
print(list_numbers)

number = int(input("Введите число, количество вхождений которого необходимо найти: ")) 
result = list_numbers.count(number)
print(f"Количество вхождений числа - > {result}")