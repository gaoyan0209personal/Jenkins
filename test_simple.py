import unittest


class TestSimple(unittest.TestCase):

    def testOne(self):
        self.assertTrue(1+1, 2)

    def testTwo(self):
        self.assertTrue('123'+"321", "123321")


if __name__ == '__main__':
    unittest.main()