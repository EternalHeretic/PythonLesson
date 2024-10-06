#Рекурсия
def get_multiplied_digits(number):

    str_number = str(number)
    first = int(str_number[0])

    while str_number.endswith('0'):
            str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(40203))
print(get_multiplied_digits(240))
print(get_multiplied_digits(23000))
print(get_multiplied_digits(42110))
print(get_multiplied_digits(98001))
print(get_multiplied_digits(450001))
print(get_multiplied_digits(451))

