import unittest
import common

class test_Sequence_Functions(unittest.TestCase):
    
    def test1(self):
        '''
        tests the prime tester function isprime in common.py
        '''
        self.assertEqual(common.isPrime(2),True) # t1 check of 2 fails

    def test2(self):
        '''tests the combination case tool'''
        self.assertEqual(common.combinations(3,3),[(0,1,2)])
        self.assertEqual(common.combinations(3,1),[(0,),(1,),(2,)])
        self.assertEqual(common.combinations(3,2),[(0,1),(0,2),(1,2)])

    def test3(self):
        '''this tests the join tool in checking that the parts of a tuple can be joined into a string'''
        
    
if __name__ == '__main__':
    unittest.main()
