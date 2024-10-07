from fake_math import divide as fk_num
from true_math import divide as tr_num

print('result1 =', fk_num(69, 3))
print('result2 =', fk_num(3, 0))
print('result3 =', tr_num(49, 7))
print('result4 =', tr_num(15, 0))


x = 10
def foo():
    global x
    x = 20
foo()
print(x)