from unirank import Ranking
import unittest

class TestUnirank(unittest.TestCase):
    def test_count(self):
        rank = Ranking()
        usa = rank.get_usa()
        count = rank.usa_total()
        self.assertEqual(len(usa), count)

if __name__ == '__main__':
  unittest.main()
