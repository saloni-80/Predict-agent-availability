import unittest
from agent import *

class AgentTest(unittest.TestCase):
    def test_getAvgWait_greaterThan1(self):
        Lambda = 3
        Mue = 2
        self.assertGreater(getAvgWait(Lambda,Mue),1)



if __name__ == '__main__':
    unittest.main()