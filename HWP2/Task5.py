# Реализуйте алгоритм перемешивания списка.

import random
order_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(order_list)
print(order_list)

# from random import randint
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(list)-1, 0, -1):
#     j = randint(0, i-1)
#     list[i], list[j] = list[j], list[i]
# print(list)