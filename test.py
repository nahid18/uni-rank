from unirank import Ranking
import unittest

class TestUnirank(unittest.TestCase):
    def test_connection(self):
        rank = Ranking()
        ua = rank.__useragent()
        self.assertGreater(len(ua), 0)

if __name__ == '__main__':
  unittest.main()
