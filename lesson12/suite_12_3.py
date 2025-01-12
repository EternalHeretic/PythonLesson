import unittest
import tests_12_3

ts = unittest.TestSuite()

ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
test_runner = unittest.TextTestRunner(verbosity=2)


if __name__ == '__main__':
    test_runner.run(ts)