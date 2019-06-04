import unittest
from src.ship import Ship


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_has(self):
        testShip = Ship()
        testShip.setCoords([[0, 1], [0, 2]])
        self.assertFalse(testShip.has(0, 0))
        self.assertTrue(testShip.has(0, 1))
        self.assertTrue(testShip.has(0, 2))


if __name__ == '__main__':
    unittest.main()
