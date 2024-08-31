my_dict = {'Vasya': 654321, 'Egor': 123456, 'Masha': 123654}
print('Dict:', my_dict)
print('Existing value:',my_dict['Egor'])
print('Not existing value:', my_dict.get('Vasyalisa'))
my_dict.update({'Kate':321456, 'Natali':654123})
print('Deleted value:', my_dict['Masha'] )
del my_dict['Masha']
print('Modified dictionary:',my_dict)


my_set_ = {'Сок',1, 1, 'Сок', 1,3.141592653589793}
print('Set:',my_set_)
my_set_.add(2)
my_set_.add('Urban')
print('Modified set:', my_set_)