# Напишите программу, удаляющую из текста все
# слова, содержащие ""абв"".
# Задачу решила пока для английской раскладки. Искала abc

with open('filenumbers3.txt', 'r') as file:
    my_string = file.readline()
print(my_string)

search_bar = input('Введите искомый элемент: ')
final_text = []
words = my_string.split(' ')
for word in words:
    if search_bar not in word:
        final_text.append(word)
print(*final_text)

data = open('filenumbers4.txt', 'w')
data.writelines(' '.join(final_text))
data.close()
