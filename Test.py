import unittest
from os import system
import time
from GHAnalysis import Run, Data


class Test(unittest.TestCase):

    def test(self):
        a = Data(".", 1)  # 用于本地测试
        self.assertEqual(a.getEventsUsers("rspt", "PushEvent"),1)


if __name__ == '__main__':
        unittest.main()