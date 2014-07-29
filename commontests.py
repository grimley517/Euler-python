import unittest
import common

class test_Sequence_Functions(unittest.TestCase):
    
    def test1(self):
        '''
        tests the prime tester function isprime in common.py
        '''
        assertEqual(common.isPrime(2),True) # t1 check of 2 fails
        
if __name__ == '__main__':
    unittest.main()
