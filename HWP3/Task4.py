# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число '))
result = ''
while num > 0:
    if num % 2 == 0:
        result = '0' + result
    else:
        result = '1' + result
    num //= 2
print(result)