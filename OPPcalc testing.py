import unittest
from OPPcalc import Data, User, Roi

class TestRoi(unittest.TestCase):
    def test_calculateRoi(self):        
        data = Data('Test1', 'Test1', 100, 100)
        self.assertEqual(data.calculateRoi(), 100)

        data2 = Data('Test2', 'Test2', 45, 80)
        self.assertEqual(data2.calculateRoi(), 56.25)

        data3 = Data('Test3', 'Test3', 90, 25)
        self.assertEqual(data3.calculateRoi(), 360)
    
if __name__ == '__main__':
    unittest.main()