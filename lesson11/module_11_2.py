# Создать персональную функции для подробной интроспекции объекта.
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

def introspection_info(obj):
  obj_type = type(obj).__name__
  value_type = None
  if hasattr(obj, 'value'):
    value_type = type(obj.value).__name__
  all_attributes = dir(obj)
  user_defined_attributes = [attr for attr in all_attributes if
                             not attr.startswith('__') and not callable(getattr(obj, attr))]
  user_defined_methods = [attr for attr in all_attributes if callable(getattr(obj, attr)) and not attr.startswith('__')]
  module = obj.__module__
  info = {
    'type': value_type if value_type else obj_type,
    'attributes': user_defined_attributes,
    'methods': user_defined_methods,
    'module': module
  }
  return info
class MyClass:
  def __init__(self, value):
    self.value = value
  def display(self):
    return f'Value: {self.value}'

# class Abra:
#   forskrin = 42
#   gdai = 'stroka'


my_obj = MyClass(42)

obj_info = introspection_info(my_obj)
print(obj_info)