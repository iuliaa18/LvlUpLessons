# Example
# a = 900
# i = 11
# while True:
#    i -= 1
#   if i == 0:
#       continue
#    if i < -10:
#         break
#    print(a, "/", i, "=", a / i)



#Задача А. Дано число n. Вывести все четные числа в интервале (0, n]
#n = int(input("Введите число:"))
#for i in range(0, n, 2):
#    if i % 2 == 0:
#        print(i)

#Задача Б. Дано число n. Вывести все делители.
n = int(input("Введите число:"))
for i in range(1, n, 1):
    if n % i == 0:
        print(i)










