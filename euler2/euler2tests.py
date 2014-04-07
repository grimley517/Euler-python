import unittest
import euler2 as e2

class runtests(unittest.TestCase):
    
    def test1(self):
        assert e2.nterm(1,2) == 3
    
    def test2(self):
        assert e2.fiblist(10) == [1,2,3,5,8] # test 2 fails - generate fibbonacci list
        
    def test3(self):
        #extract even numbered terms
        print e2.fiblisteven2(10)
        assert e2.fiblisteven2(10) == [2,8]#test 3 fails - extraction of even numbers
        
        
    def test4(self):
        #sum of list fn
        assert e2.sumof(e2.fiblisteven2(10))==10#test 4 fails - summation of list
    
    def testfinal(self):
        print (e2.sumof(e2.fiblisteven2(4000000)))
        
    
if __name__ == '__main__':
    unittest.main()