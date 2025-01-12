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