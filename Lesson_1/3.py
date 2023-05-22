# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

num = int(input("Введите номер билета: "))
if len(str(num)) == 6: # условие на то, чтобы количество чисел в билете было равно 6 
# if num >= 100000 and num <= 999999: - альтернативный вариант
    if num // 100000 + num // 10000 % 10 + num // 1000 % 10 == num % 1000 // 100 + num % 100 // 10 + num % 10:
    # условие сравнивает суммы первых и последних трех чисел билета
        print(f"Вам повезло! Билет {num} счастливый!")
    else: 
        print(f"Билет {num} несчастливый. Испытайте удачу в другой раз!")
else: 
    print("Номер билета введен некорректно!")
