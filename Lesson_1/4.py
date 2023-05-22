# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Введите количество долек, на которые необходимо разломить шоколадку: "))

'''''''''''''''
1. Независимо от длины и ширины невозможно поделить шоколадку на долек меньше 1, 
а также на количество долек больше или равному, чем есть в шоколадке.
2. Если длина ИЛИ ширина шоколадки равна 1, в этом случае может быть отделена 1 долька 
(исключение - шоколадка размером 1*1 (пункт 1))
3. Если длина И ширина шоколадки больше 1, то невозможно поделить шоколадку на 1 дольку. 
4. Невозможно поделить шоколадку одним разломом по прямой на количество долек меньше, 
чем длина ИЛИ ширина шоколадки.
'''''''''''''''

if k < 1 or n*m <= k: # пункт 1
    print("Введено некорректное количество долек, на которые необходимо разломить шоколадку!")
else:
    if n == 1 or m == 1: # пункт 2
        print(f"Разделить шоколадку размером {n} * {m} на {k} долек(ки) одним разломом по прямой возможно.")
    elif k > 2: # пункт 3
        if k % n == 0 or k % m == 0: # пункт 4
            print(f"Разделить шоколадку размером {n} * {m} на {k} долек(ки) одним разломом по прямой возможно.")
        else:
            print(f"Разделить шоколадку размером {n} * {m} на {k} долек(ки) одним разломом по прямой невозможно.")
    else: 
        print(f"Разделить шоколадку размером {n} * {m} на {k} долек(ки) одним разломом по прямой невозможно.")