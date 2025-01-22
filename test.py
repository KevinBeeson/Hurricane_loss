#this is the test file for gethurricaneloss.py
import unittest
import gethurricaneloss
import numpy as np
import logging
logging.getLogger().setLevel(logging.INFO)

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    #see if hurricane_rate_florida is int and greater or equal to 0
    def test_hurricane_rate_florida(self):
        self.assertTrue(gethurricaneloss.hurricane_rate_florida(2) >= 0)
        self.assertTrue(isinstance(gethurricaneloss.hurricane_rate_florida(2), (int, np.integer)))
    #see if hurricane_rate_gulf_states is int and greater or equal to 0
    def test_hurricane_rate_gulf_states(self):
        self.assertTrue(gethurricaneloss.hurricane_rate_gulf_states(2) >= 0)
        self.assertTrue(isinstance(gethurricaneloss.hurricane_rate_gulf_states(2), (int, np.integer)))
    #see if economic_loss_florida is float and greater or equal to 0
    def test_economic_loss_florida(self):
        self.assertTrue(gethurricaneloss.economic_loss_florida(2.3,1) >= 0)
        self.assertTrue(isinstance(gethurricaneloss.economic_loss_florida(2,1), (float, np.floating)))
    #see if economic_loss_gulf_states is float and greater or equal to 0
    def test_economic_loss_gulf_states(self):
        self.assertTrue(gethurricaneloss.economic_loss_gulf_states(2.3,1) >= 0)
        self.assertTrue(isinstance(gethurricaneloss.economic_loss_gulf_states(2,1), (float, np.floating)))


if __name__ == '__main__':
    unittest.main()