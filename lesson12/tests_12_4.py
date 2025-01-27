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

import logging
import unittest
from rt_with_exceptions import Runner, Tournament

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Test Runner", -10)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}", exc_info=True)

    def test_run(self):
        try:
            runner = Runner(123, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}", exc_info=True)

    def test_runner_creation(self):
        try:
            runner = Runner("Valid Runner", 10)
            self.assertEqual(runner.name, "Valid Runner")
            self.assertEqual(runner.speed, 10)
            logging.info('"test_runner_creation" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка при создании объекта Runner: {e}", exc_info=True)

    def test_runner_str(self):
        try:
            runner = Runner("Test Runner", 10)
            self.assertEqual(str(runner), "Test Runner")
            logging.info('"test_runner_str" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в методе __str__: {e}", exc_info=True)

    def test_runner_eq(self):
        try:
            # Проверка метода __eq__
            runner1 = Runner("Test Runner", 10)
            runner2 = Runner("Test Runner", 5)
            self.assertTrue(runner1 == runner2)
            self.assertTrue(runner1 == "Test Runner")
            logging.info('"test_runner_eq" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в методе __eq__: {e}", exc_info=True)

class TournamentTest(unittest.TestCase):
    def test_tournament_start(self):
        try:
            runner1 = Runner("Runner 1", 10)
            runner2 = Runner("Runner 2", 5)
            tournament = Tournament(100, runner1, runner2)
            results = tournament.start()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[1].name, "Runner 1")
            self.assertEqual(results[2].name, "Runner 2")
            logging.info('"test_tournament_start" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в методе start: {e}", exc_info=True)

    def test_tournament_no_participants(self):
        try:
            tournament = Tournament(100)
            results = tournament.start()
            self.assertEqual(len(results), 0)
            logging.info('"test_tournament_no_participants" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в турнире без участников: {e}", exc_info=True)

if __name__ == '__main__':
    unittest.main()