from unirank import Ranking
import unittest

class TestUnirank(unittest.TestCase):
    def test_connection(self):
        rank = Ranking()
        ua = rank._useragent()
        print(ua)
        self.assertGreater(len(ua), 0)

if __name__ == '__main__':
  unittest.main()
