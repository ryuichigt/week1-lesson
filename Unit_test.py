import unittest
from vacation import Vacation

class TestTashizan(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_vacation(self):
        """test method for tashizan
        """
        vacation = [7,3]
        day = [19,20,21,22,23,24,25]
        rainy_percent = [0,0,60,30,10,10,90]

        expected = "22 24"


        actual = Vacation(vacation, rainy_percent, day)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()


