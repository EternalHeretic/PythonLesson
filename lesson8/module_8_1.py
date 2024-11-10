# "Программистам всё можно":
# Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int) и строку(str)?
# Давайте исправим это недоразумение!
#
# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)
#
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух данных вместе
# (в том же порядке). Во всех остальных случаях выполнять стандартные действия.

def add_everything_up(a, b):
    try:
        a + b
    except TypeError as err:
        print(f'Возникла ошибка: {err}. Тип первого аргумента: {type(a)}, тип второго аргумента: {type(b)}')
        return f'{str(a)}{str(b)}\n'
    else:
        if type(a) or type(b) is float:
            return round(a + b, 3)
        else:
            return a + b
    finally:
        if type(a) is int and type(b) is str:
            print(f'Эта функция может также складывать числа и строки, результат: {a + len(b)}')
        elif type(a) is str and type(b) is int:
            print(f'Эта функция может также складывать строки и числа, результат: {len(a) + b}')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
