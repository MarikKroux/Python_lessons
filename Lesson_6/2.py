# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

list_result = []
count = int(input("Введите количество элементов: "))
start = int(input("Введите минимальное генерируемое число: "))
end = int(input("Введите максимальное генерируемое число: "))
min_ = int(input("Введите минимум диапазона: "))
max_ = int(input("Введите максимум диапазона: "))

list_numbers = [randint(start, end) for i in range(count)]
print(f"Сгенерированный список: {list_numbers}")

for i in range(len(list_numbers)):
    if min_ <= list_numbers[i] <= max_:
        list_result.append(i)
print(f"Индексы элементов, подходящих под условие: {list_result}")