#text.count - подсчитывает количество вхождений одной строки в другую;
#text.format - форматирование строки;
#Функция len - позволяет узнать количество символов (длину строки);

#Задание А. Вводится n строк. Вывести количество любого символа.
#Задание Б. Вводится n строк, каждая строка - одно слово. Составить из них предложение с пробелами и точкой в конце.
n = int(input())
text = ""
for i in range(n):
    text += input()
    text += " "
print(f"{text}.")
print(f"{text}".count("а"))




