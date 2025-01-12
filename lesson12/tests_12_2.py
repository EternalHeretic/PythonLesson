# Задача:
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
# Изменения в классе Runner:
# Появился атрибут speed для определения скорости бегуна.
# Метод __eq__ для сравнивания имён бегунов.
# Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников.
# Также присутствует метод start, который реализует логику бега по предложенной дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
# setUp - метод, где создаются 3 объекта:
# Бегун по имени Усэйн, со скоростью 10.
# Бегун по имени Андрей, со скоростью 9.
# Бегун по имени Ник, со скоростью 3.
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса
# Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue,
# в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
# Усэйн и Ник
# Андрей и Ник
# Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.
#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
# В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.
# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
#
# Примечания:
# Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов и
# наличие всех перечисленных переопределённых методов из класса TestCase.

import runner_and_tournament as rt
import unittest

class TournamentTest(unittest.TestCase):
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

    def test_tournament_1(self):
        _tournament = rt.Tournament(90, self.runner_1, self.runner_3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner_3.name)

    def test_tournament_2(self):
        _tournament = rt.Tournament(90, self.runner_2, self.runner_3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner_3.name)

    def test_tournament_3(self):
        _tournament = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner_3.name)