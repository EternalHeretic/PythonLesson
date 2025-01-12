# Задача "Логирование бегунов":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
# Уровень - INFO
# Режим - запись с заменой('w')
# Название файла - runner_tests.log
# Кодировка - UTF-8
# Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте отрицательное значение в speed.
# В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
# test_run:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте что-то кроме строки в name.
# В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
# Пример результата выполнения программы:
# Пример полученного файла логов runner_tests.log:

import inspect
import logging
from rt_with_exceptions import Runner
import unittest


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                            format='%(asctime)s | %(levelname)s | %(message)s', encoding='UTF-8')

    def test_walk(self):
        try:
            r1 = Runner('Tom', -5)
            for _ in range(10):
                r1.walk()
            logging.info(f'метод {inspect.currentframe().f_code.co_name} выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)
        self.assertEqual(50, r1.distance,
                         f'test Runner.walk() is failed. Expected: 50, Actual: {r1.distance}.')

    def test_run(self):
        try:
            r2 = Runner(2)
            for _ in range(10):
                r2.run()
            logging.info(f'метод {inspect.currentframe().f_code.co_name} выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        self.assertEqual(100, r2.distance,
                         f'test Runner.run() is failed. Expected: 100, Actual: {r2.distance}.')


if __name__ == '__main__':
    unittest.main()