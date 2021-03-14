from unirank import Ranking
import unittest

class TestUnirank(unittest.TestCase):
    def test_connection(self):
        rank = Ranking()
        status = rank._connection()
        self.assertEqual(status, 200)

if __name__ == '__main__':
  unittest.main()
