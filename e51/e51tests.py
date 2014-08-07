import e51
import unittest

class testSequence (unittest.testSequence):
    def setup(self)
        pass

    def test_main(self):
        '''as per question the lowest prime of 13 would give 6 primes'''
        self.assertEqual(e51.numPrimes(13)==6)#13 does not give 6 primes

if __name__ =="__main__":
    unittest.main()