#Задача Б. Даны два числа n и m, первое число - размер вклада пользователя, второе число - срок вклада в годах,
# соответственно. Вывести размер вклада через число лет.

bank_percent = 0.1
def read_input():
    n = int(input())
    m = int(input())
    return n, m
def calculate(n, m):
    total_money = n
    for i in range(m):
        total_money = total_money + total_money * 0.1
        print(total_money)
n, m = read_input()
calculate(n, m)