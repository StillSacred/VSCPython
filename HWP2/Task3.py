# Задайте список из n чисел последовательности (1+ 1 / n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 2, 2: 2, 3: 2, 4:2, 5: 2, 6: 3} -> 13

num = int(input("Введите число: "))
sequence_list = {i:round((1+ 1 / i)**i) for i in range(1, num+1)}
print(sequence_list, "Сумма значений: ", sum(sequence_list.values()))

# def func(num):
#     if num == 0:
#         return 0
#     return (1+1/num)**num + func(num-1)


# n = int(input('Введите число: '))
# result = {}
# for i in range(1, n+1):
#     result[i] = round(func(i), 0)
# print(result)