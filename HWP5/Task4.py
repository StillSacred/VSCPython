# Задача №41: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:          12W1B12W3B24W1B14W

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")


# RLE запаковщик

# def rle_crypt(file_name: str):
#     with open(file_name, 'r') as file:
#         data = file.readlines()
#     count = 1
#     string = ''
#     for i in data:
#         for j in range(len(i)-1):
#             if i[j] == i[j+1]:
#                 count += 1
#             else:
#                 string += str(count) + i[j]
#                 count = 1
#         string += str(count) + i[j+1]
#     with open('crypted_data.txt', 'w') as file:
#         file.write(string)
# rle_crypt('data.txt')


# RLE распаковщик

# def rle_decrypt(file_name: str):
#     with open(file_name, 'r') as file:
#         cr_data = ''.join(file.readlines())
#     arr = []
#     string = ''
#     for i in range(len(cr_data)):
#         if cr_data[i].isdigit():
#             string += cr_data[i]
#         else:
#             arr.append([int(string), cr_data[i]])
#             string = ''
#     decr_data = ''
#     for i in arr:
#         for j in range(len(i)-1):
#             decr_data += i[j] * i[j+1]
#     print(decr_data)
#     with open('decrypted_data.txt', 'w') as file:
#         file.write(decr_data)
# rle_decrypt('crypted_data.txt')