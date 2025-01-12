import inspect
import logging
from runner_and_tournament import Runner
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