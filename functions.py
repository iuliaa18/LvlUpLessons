# def название функции(аргументы):
# Example:
#def two_numbers_sum(a, b):
#    print(a + b)
#two_numbers_sum(6, 8)

#def read_input():
#    n = int(input())
#    my_list = []
#    for i in range(n):
#        number = int(input())
#        my_list.append(number)
#    return my_list

#my_list = read_input()
#for i in my_list:
#    print(i**2)

#Задача А.
def read_input():
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    c = input("Введите символ операции: ")
    my_list = []
    return a, b, c
def calculate (a, b, c):
    if c == "+":
        print(a + b)
    elif c == "-":
        print (a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    else:
        print("Некорректный ввод.")
a, b, c = read_input()
result = calculate(a, b, c)



























