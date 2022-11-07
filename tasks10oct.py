# 1. Напишите программу, которая будет запрашивать у пользователя длины всех трех сторон треугольника
# и выдавать сообщение о том, к какому типу он относится.

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# 2. Напишите программу для изображения стандартной таблицы умножения от единицы до девяти.
# При этом ваша таблица должна иметь заголовки над первой строкой и слева от первого столбца.

# c = "          Таблица умножения"
# print(c)
# for a in range(1, 10):
#     for b in range(1, 10):
#         print(a*b, end="\t")
#     print()

# Напишите программу, которая будет запрашивать у пользователя числа, пока он не пропустит ввод. Сначала на экран должно
# быть выведено среднее значение введенного ряда чисел, после этого друг за другом необходимо вывести список чисел ниже
# среднего, равных ему и выше среднего. Каждый список должен иметь соответствующий заголовок.


import statistics
a = [int(i) for i in input().split()]
b = statistics.fmean(a)
print("Среднее значение введеного ряда чисел: ", b)

less = []
more = []

for i in a:
    if i < b or i ==b:
        less.append(i)
    else:
        more.append(i)

print(f'"Числа меньше среднего значения:" {less}')
print(f'"Числа больше среднего значения:" {more}')