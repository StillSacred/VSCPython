# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
print(list)
sum = 0 
for i in range(1, len(list), 2):
    sum = sum + list[i]
print(sum)

# from random import randint

# nums = []
# for i in range(randint(4, 8)):
#     nums.append(randint(5, 11))

# result = 0
# for i in range(len(nums)):
#     if i % 2 != 0:
#         result += nums[i]
# print(nums, result, sep=' -> ')