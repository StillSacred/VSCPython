# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

from itertools import zip_longest
from random import randint

def get_coefs(x):
    list = [randint(0, 100) for i in range(x+1)]
    while list[0] == 0:
        list[0] = randint(0, 100)
    return list

k = int(input('Укажите степень многочлена: '))

if k == 0:
    with open('task4.txt', 'w') as f:
        f.write(f'c = {randint(0, 100)}')

elif k == 1:
    coefs = get_coefs(k)

    with open('task4.txt', 'w') as f:
        f.write(f'{coefs[0]}*x + {coefs[1]} = 0')

elif k > 1:
    coefs = get_coefs(k)
    coefs = [str(i) for i in coefs]

    arr = [f'*x^{i} + ' for i in range(k, 1, -1)]
    arr.append('*x + ')
    arr2 = [list(i) for i in list(zip_longest(coefs, arr, fillvalue=''))]

    result = ''
    for list in arr2:
        result += ''.join(list)
    with open('task4.txt', 'w') as f:
        f.write(f'{result} = 0')