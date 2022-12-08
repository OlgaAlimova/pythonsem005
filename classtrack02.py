# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

with open('filenumbers2.txt', 'r') as file:
    my_string = file.readline()

my_list = list(map(int, my_string.split()))
print(my_list)

find = int(input('Введите стартовый элемент: '))
index = 0
for i, item in enumerate(my_list):
    if item == find:
        index = i
        break

def filternumber(list1: list) -> list:
    temp = list1[0]
    new_list = []
    new_list.append(list1[0])
    for i in range(1, len(list1)):
        if list1[i] - 1 == temp:
            new_list.append(list1[i])
            temp = list1[i]
    return new_list

new_list = my_list[index:]
print(filternumber(new_list))



