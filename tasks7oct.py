# 1. Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

# n = int(input("Количество элементов в списке:"))
# my_list = []
# for i in range(n):
#  element = input()
#  my_list.append(element)
# print(my_list)
# def change(my_list):
#  my_list[0], my_list[-1] = my_list[-1], my_list[0]
#  return my_list
# print(change(my_list))

# 2. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
# и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них
# недостаточно соседей.

# a = [int(i) for i in input().split()]
# counter = 0
# for i in range(1, len(a) - 1):
#     if a[i-1] < a[i] > a[i+1]:
#         counter += 1
# print(counter)

# 3. Дан список чисел, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

a = input().split()
counter = 0
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        counter += 1
print(counter + 1)
