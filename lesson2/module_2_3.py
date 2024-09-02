my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
len_list = len(my_list)
print('Список четных положительных чисел:')
while i != len_list:
    if (my_list[i] % 2 == 0) and my_list[i] > 0:
        print(my_list[i])
        i = i+1
    else:
        i = i + 1