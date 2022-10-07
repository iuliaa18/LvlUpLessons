#Задача Б. Дан список чисел. Выведите все четные числа.
n = int(input())
my_list = []
for i in range(n):
    number = int(input())
    my_list.append(number)
for i in my_list:
    if i % 2 == 0:
        print(i)
