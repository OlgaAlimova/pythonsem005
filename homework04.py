# Реализуйте RLE алгоритм: реализуйте модуль сжатия и
# восстановления данных

with open('filenumbers5.txt', 'r') as file:
    my_string = file.readline()

print(my_string)

my_list = []
letter = my_string[0]
print(letter)
count = 0
for simbol in range(len(my_string)):
    print(f'my_string[simbol] = {my_string[simbol]}')
    if my_string[simbol] == letter:
        count += 1
    else:
        print(f'count = {count}')
        my_list.append(count)
        my_list.append(letter)
        letter = my_string[simbol]
        print(f'letter = {letter}')
        count = 1

print(count)
print(letter)
my_list.append(count)
my_list.append(letter)

print(my_list)
print(*my_list, sep='')

def convertlist(list1):
    stroka = ''
    for i in list1:
        stroka += str(i)
    return stroka

final = convertlist(my_list)
print(final)

with open('filenumbers6.txt', 'w') as file:
    file.write(final)

with open('filenumbers6.txt', 'r') as file:
    mi_string = file.readline()
print(mi_string)

new_list = []
list_letter_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(mi_string)):
    if mi_string[i] in list_letter_num:
        new_list.append(int(mi_string[i]))
    else:
        new_list.append(mi_string[i])
print(f'new_list = {new_list}')
list_fin = [new_list[0]]
for j in range(1, len(new_list)):
    if (new_list[j - 1] in list_numbers) and (new_list[j] in list_numbers):
            num = new_list[j - 1] * 10 + new_list[j]
            list_fin.pop(j-1)
            list_fin.append(num)
    else:
        list_fin.append(new_list[j])
print(f'list_fin = {list_fin}')


list_couples = []
for k in range(len(list_fin)):
    if k % 2 == 0:
        temp = list_fin[k]
        couples = list_fin[k+1]
        for z in range(temp):
            list_couples.append(couples)
print(f'list_couples = {list_couples}')
print(*list_couples, sep='')

final_rle = convertlist(list_couples)
print(f'final_rle = {final_rle}')

with open('filenumbers7.txt', 'w') as file:
    file.write(final_rle)


