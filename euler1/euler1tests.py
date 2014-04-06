import unittest
import euler1

class runtests(unittest.TestCase):
    
    def test1(self):
        mults = euler1.mults(3,10)
        try:
            assert mults == [3,6,9] # test 1 multiples of 3 under 10 fails
        except AssertionError as e:
            print (mults)
            print ('should be [3,6,9]')
            raise (AssertionError)
    
    def test2(self):
        mults = euler1.mults(5,10)
        try:
            assert mults == [5] # test 2 multiples of 5 under 10 fails
        except AssertionError as e:
            print (mults)
            print ('should be [5]')
            raise (AssertionError)

    def test3(self):
        # sum of mults(3,10) should be 18
        mults = euler1.mults(3,10)
        assert euler1.sumof(mults) == 18 #test 3 fails - summation over list
    
    def testanswer(self):
        tar = 1000
        m3 = euler1.mults(3,tar)
        m5 = euler1.mults(5,tar)
        m15 = euler1.mults(15,tar)
        answer = euler1.sumof(m3) + euler1.sumof(m5) - euler1.sumof(m15)
        print (answer)
    
if __name__ == '__main__':
    unittest.main()