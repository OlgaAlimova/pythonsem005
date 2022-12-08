# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.

with open('filenumbers1.txt', 'r') as file:
    my_string = file.readline()

my_list = list(map(int, my_string.split()))
print(my_list)

def find_number(fn_list: list) -> int:
    for i in range(1, len(fn_list)):
        if fn_list[i] - 1 != fn_list[i-1]:
            return fn_list[i] - 1

out_number = find_number(my_list)
print(out_number)


