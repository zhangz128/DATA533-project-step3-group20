import unittest
from test_store import TestAccount  
from test_transaction import TestTransaction  

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAccount))
    suite.addTest(unittest.makeSuite(TestTransaction))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
