import unittest, sys, os, xmlrunner
sys.path.append('stripe')
from stripe_test import TestStripe

if __name__ == '__main__':
    testSuite = unittest.TestLoader().loadTestsFromTestCase(TestStripe)
    xmlrunner.XMLTestRunner(output='reports').run(testSuite)
    
