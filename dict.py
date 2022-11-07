# А. Дан список с посетителями ветеринарной клиники в формате - Кличка Возраст Имя Фамилия. Оптимизировать
# хранение так, чтобы у каждого владельца был список собак.

# my_dict = {'Алексей Егоров': 'Мартин 5 лет', 'Анна Самохина': 'Фродо 3 года'}
# person = input()
# if person in my_dict:
#         x = my_dict[person]
#         print(x)
# else:
#       print("Не найдено.")


# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.

# my_dict = {}
# letter = input()
# for i in letter:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# print(my_dict)


# Задание "Игральные кости"

import random

def dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a + b

my_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

expected = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36,
            11: 2 / 36, 12: 1 / 36}
for i in range(1000):
    t = dice()
    my_dict[t] = my_dict[t] + 1
for k, v in my_dict.items():
    my_dict[k] = v / 1000 * 100
print('Результат\tРезультат симуляции')
for k, v in my_dict.items():
    print(f"\t{k}              {v:.2f}")


