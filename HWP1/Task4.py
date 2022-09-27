# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (х и у)

# quarter = int(input('Введите порядковый номер четверти\n'))
# while not 1 <= quarter <= 4:
#     quarter = int(input('Введено неверное значение \nПовторите ввод\n'))
# if quarter == 1:
#     print('X(0, +inf) Y(0, +inf)')
# elif quarter == 2:
#     print('X(-inf, 0) Y(0, +inf)')
# elif quarter == 3:
#     print('X(-inf, 0) Y(-inf, 0)')
# elif quarter == 4:
#     print('X(0, +inf) Y(-inf, 0)')

x = int(input('Введите № четверти: '))

range_of_points = {
    1: "Первая четверть состоит из x>0 and y>0 ",
    2: "Вторая четверть состоит из x<0 and y>0 ",
    3: "Третья четверть состоит из x<0 and y<0 ",
    4: "Четвертая четверть состоит из x>0 and y<0 "
}
if 0<x<5: print(range_of_points[x])
else: print(f"Значение {x} не является четвертью")