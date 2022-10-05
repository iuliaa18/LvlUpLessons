a = int(input("Введите число:"))
b = int(input("Введите число:"))
c = int(input("Введите число:"))
if a > b > c:
    print(c, b, a)
elif a > c > b:
    print(b, c, a)
elif b > c > a:
    print(a, c, b)
elif c > a > b:
    print(b, a, c)
else:
    print(a, b, c)

