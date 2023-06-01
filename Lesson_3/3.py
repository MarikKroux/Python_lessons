# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12

# word = input("Введите слово заглавными буквами: ")

# isCyrillic = bool(re.search('[а-яА-Я]', word))

# # word = list(str_word)

# result = 0

# list_eng_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']   # 1 очко
# list_eng_2 = ['D', 'G']                                           # 2 очка
# list_eng_3 = ['B', 'C', 'M', 'P']                                 # 3 очка
# list_eng_4 = ['F', 'H', 'V', 'W', 'Y']                            # 4 очка
# list_eng_5 = ['K']                                                # 5 очков
# list_eng_6 = ['J', 'X']                                           # 8 очков
# list_eng_7 = ['Q', 'Z']                                           # 10 очков

# list_rus_1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']        # 1 очко
# list_rus_2 = ['Д', 'К', 'Л', 'М', 'П', 'У']                       # 2 очка
# list_rus_3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']                            # 3 очка
# list_rus_4 = ['Й', 'Ы']                                           # 4 очка
# list_rus_5 = ['Ж', 'З', 'Ц', 'Х', 'Ч']                            # 5 очков
# list_rus_6 = ['Ш', 'Э', 'Ю']                                      # 8 очков
# list_rus_7 = ['Ф', 'Щ', 'Ъ']                                      # 10 очков

# if lang == "ENG":
#     for letter in str_word:
#         if letter in list_eng_1:
#             result += 1
#         elif letter in list_eng_2:
#             result += 2
#         elif letter in list_eng_3:
#             result += 3
#         elif letter in list_eng_4:
#             result += 4
#         elif letter in list_eng_5:
#             result += 5
#         elif letter in list_eng_6:
#             result += 8
#         elif letter in list_eng_7:
#             result += 10
#         else:
#             print("Что-то вы ввели не то и не туда)))")
#     print(result)

# elif lang == "RUS":
#     for letter in str_word:
#         if letter in list_rus_1:
#             result += 1
#         elif letter in list_rus_2:
#             result += 2
#         elif letter in list_rus_3:
#             result += 3
#         elif letter in list_rus_4:
#             result += 4
#         elif letter in list_rus_5:
#             result += 5
#         elif letter in list_rus_6:
#             result += 8
#         elif letter in list_rus_7:
#             result += 10
#         else:
#             print("Что-то вы ввели не то и не туда)))")
#     print(result)

list_rus = {1:"АВЕИНОРСТ",
                2:"ДКЛМПУ",
                3:"БГЁЬЯ",
                4:"ЙЫ",
                5:"ЖЗХЦЧ",
                8:"ШЭЮ",
                10:"ФЩЪ"}

list_eng = {1:"AEIOULNSTR",
                2:"DG",
                3:"BCMP",
                4:"FHVWY",
                5:"K",
                8:"JX",
                10:"QZ"}

lang = int(input("Выберите язык (RUS - 1, ENG - 0): "))
if lang == 1 or lang == 0:
    word = input("Введите слово: ").upper()
    
    sum_word = 0
    if lang == 1:
        for i in word:
            for j, k in list_rus.items():
                if i in k:
                    sum_word += j
    else:
        for i in word:
            for j, k in list_eng.items():
                if i in k:
                    sum_word += j   
    print(f"Стоимость слова: {sum_word}")
else: 
    print("Выбран неверный язык.")
