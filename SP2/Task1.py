# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

# n = int(input('Введите число N: '))
# num = 1
# print(num, end=', ')

# for i in range(N - 1):
#     num = num * -3
#     print(num, end=', ')



# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int(input("Введите число: "))
# d = {i : 3*i + 1 for i in range(1,number+1)}
# print(f"Итоговая последовательность: {d}")

# n= int(input())
# for i in range(n):
#     print(f'{i}- {3 * i + 1}', end = '; ')

# x = int(input('введите число: '))
# dic = {}
# for i in range(1,x+1):
#     dic[i] = 3 * i + 1
#     i += 1 - не надо
# print(dic)

# def PrintList (spisok):
#     for i in range(len(spisok)):
#         print(f'{i+1}: {spisok[i]}', end='    ')

# n=int(input('Введите число: '))
# spisok=[]

# for i in range (1,n+1):
#     spisok.append(3*i+1) 

# PrintList(spisok)



# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# s = input("Введите 1ую строку: ").split()
# t = input("Введите 2ую строку: ").split()
# def str_count_two(str, substr):
#     count = 0
#     i = -1
#     while True:
#         i = str.find(substr, i+1)
#         if i == -1:
#             return count
#         count += 1
 
# print(str_count_two(s, t))

# str1 = input("Введите 1ую строку: ").split()
# str2 = input("Введите 2ую строку: ").split()
# total = 0
# for i in range(len(str1)):
#     for j in range(len(str2)):
#         if str1[i] == str2[j]:
#             total += 1
# print(total)

# for i in test_str: 
#     if i == 't': 
#         count = count + 1

# a = input("Введите 1ую строку: ")
# b = input("Введите 2ую строку: ")
# print(b.count(a))

# word = input('Введите слово: ')
# sub = input('Введите второе слово: ')

# print(f'Слово "{sub}" встерчается {word.count(sub)} раз.')



# Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 
# 60
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести стоимость строки.
# Тестовые данные 
# Sample Input 1:
# Привет, как дела?!
# Sample Output 1:
# 10 р. 80 коп.
# Sample Input 2:
# Тимур - лучший математик на свете!!
# Sample Output 2:
# 21 р. 0 коп.

# text = input(input('Введите текст: '))
# rub = len(text) * 0.6
# kop = len(text) * 60 % 100
# print(int(rub), 'р.', kop, 'коп.')

# print(len(input('Введите текст: ')))


# Количество слов
# Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.
# Формат входных данных
# На вход программе подается строка.
# Формат выходных данных
# Программа должна вывести количество слов в строке.
# Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).
# Примечание 2. Решите задачу в одну строчку кода.
# Тестовые данные 
# Sample Input 1:
# Hello world
# Sample Output 1:
# 2
# Sample Input 2:
# Timur forever young
# Sample Output 2:
# 3

# print(input('Введите текст: ').count(' ') + 1)