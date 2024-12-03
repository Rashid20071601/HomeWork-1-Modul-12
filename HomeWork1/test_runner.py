import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = runner.Runner('Name1')
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = runner.Runner('Name2')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)
        # self.assertEqual(run.distance, 1100)

    def test_challenge(self):
        run1 = runner.Runner('Name3.1')
        run2 = runner.Runner('Name3.2')
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__':
    unittest.main()