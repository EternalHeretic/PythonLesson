immutable_var_ = 1, 54, "Urban", True
print('Immutable tuple:',immutable_var_)

#TypeError: 'tuple' object does not support item assignment
# immutable_var_[1] = 'Egor'
# immutable_var_[3] = False
# print(immutable_var_)

mutable_list_ = list(immutable_var_)
mutable_list_[1] = "Win"
mutable_list_.insert(4, 2024)
print('Mutable list:',mutable_list_)