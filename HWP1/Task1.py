# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным

while True:
    user_week = int(input("Введите порядковый номер дня недели от 1 до 7: "))
    if 1 <= user_week <= 7:
        break

days_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" ]

if 6 <= user_week <= 7:
    print(f"{days_week[user_week - 1]}, выходной.")
else: print(f"{days_week[user_week - 1]}, рабочий день.")

# print('Введите номер дня недели')
# day_number = int(input())
# while day_number < 1 or day_number > 7:
#     print('Введен неверный номер дня недели, повторите ввод')
#     day_number = int(input())
# else:
#     if day_number == 6 or day_number == 7:
#         print('Это выходной день')
#     else:
#         print('Это будний день')