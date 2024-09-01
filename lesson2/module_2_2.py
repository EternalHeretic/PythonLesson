first = int(input('Введите первое значение:'))
second = int(input('Введите второе значение:'))
third = int(input('Введите третье значение:'))

if first == second == third:
    print('3')
elif ((first == second) and (second!= third)) or ((first != second) and (second == third)) or ((first == third) and (third != second)):
    print('2')
else: print('0')
