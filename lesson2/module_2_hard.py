import random

def get_random_first_number_code():
    numbers = list(range(3, 21))
    random_result = random.choice(numbers)
    return random_result

n = get_random_first_number_code()
print('Первое число:', n)

first_code = list(range(1, n))
second_code = list(range(1, n))
matrix = []
result = ''

for i in first_code:
    for j in second_code:
        fc = i
        sc = j
        if fc >= sc:
            continue
        else:
            divisor_factor = n % (fc + sc)
            if divisor_factor == 0:
                matrix.append([fc, sc])
                result = result + str(fc) + str(sc)
print('Пары числе', *matrix)
print('Второе число', result)