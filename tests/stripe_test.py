import unittest, sys, os
from stripe import Stripe

class TestStripe(unittest.TestCase):
    """

    A test class for the stripe module

    """

    def setUp(self):
        pass

    def testSanity(self):
        self.assertEqual(0, 0)
