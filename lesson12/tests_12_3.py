# Задача "Заморозка кейсов":
# Подготовка:
# В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
# Часть 1. TestSuit.
# Создайте модуль suite_12_3.py для описания объекта TestSuite.
# Укажите на него переменной с произвольным названием.
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
# Часть 2. Пропуск тестов.
# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod),
# который при значении is_frozen = False будет выполнять тесты,
# а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
# Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
# Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
# Пример результата выполнения тестов:
# Вывод на консоль:
# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s OK (skipped=3)


import runner_and_tournament as rt
from runner_and_tournament import Runner
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    def setUp(self):
        self.runner_tom = Runner('Tom')
        self.runner_petya = Runner('Petya')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        for _ in range(10):
            self.runner_tom.walk()
        self.assertEqual(50, self.runner_tom.distance,
                         f'test Runner.walk() is failed. Expected: 50, Actual: {self.runner_tom.distance}.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        for _ in range(10):
            self.runner_tom.run()
        self.assertEqual(100, self.runner_tom.distance,
                         f'test Runner.run() is failed. Expected: 100, Actual: {self.runner_tom.distance}.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        for _ in range(10):
            self.runner_tom.run()
            self.runner_petya.walk()
        self.assertNotEqual(self.runner_tom.distance, self.runner_petya.distance,
                            'test Runner.run() and Runner.walk() is failed. Expected: Not equal, Actual: Equal.')


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(*cls.all_results, sep='\n')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        _tournament = rt.Tournament(90, self.runner_1, self.runner_3)
        self.all_results.append(_tournament.start())

        self.assertTrue(self.all_results[-1][2], self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        _tournament = rt.Tournament(90, self.runner_2, self.runner_3)
        self.all_results.append(_tournament.start())

        self.assertTrue(self.all_results[-1][2], self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        _tournament = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.append(_tournament.start())

        self.assertTrue(self.all_results[-1][3], self.runner_3.name)


if __name__ == '__main__':
    unittest.main()