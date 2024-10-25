def custom_write(file_name, strings):
    strings_positions = {}
    str_num = 0
    file = open(file_name, 'a', encoding='utf-8')

    for s in strings:
        str_num += 1
        start_byte = file.tell()
        file.write(f'{s}\n')
        strings_positions[(str_num, start_byte)] = s

    file.close()
    return strings_positions

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)