import unittest
from unittest.mock import patch
from user.transaction import transaction
from admin.card import Card
from admin.card import User
import time

test_card = Card('123456', '1234', 100)
test_user = User('Test User', '1234567890', '555-5555', test_card)
test_users = {'123456': test_user}

class TestTransaction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Set up class resources...")

    @classmethod
    def tearDownClass(cls):
        print("Cleaning up class resources...")

    def setUp(self):
        self.allUser = {'123456': test_user}
        self.transaction = transaction(self.allUser)

    def tearDown(self):
        test_user.card.cardMoney = 100
        self.allUser = None
        del self.transaction

    @patch('builtins.input', side_effect=['123456', '1234', '50'])
    def testDeposit(self, mockinputs):
        with patch('builtins.input', side_effect=['123456', '1234', '-50']):
            self.transaction.deposit()
            self.assertEqual(test_user.card.cardMoney, 100)
            self.assertIsNotNone(test_user)
            self.assertIsNotNone(test_user.card)
            self.assertFalse(test_user.card.cardLock)
    
    @patch('builtins.input', side_effect=['123456', '1234', '50'])
    def testWithdraw(self, mockinputs):
        with patch('builtins.input', side_effect=['123456', '1234', '50']):
            self.transaction.withdraw()
            self.assertEqual(test_user.card.cardMoney, 50)
            self.assertIsNotNone(test_user)
            self.assertIsNotNone(test_user.card)
            self.assertFalse(test_user.card.cardLock)

    @patch('builtins.input', side_effect=['123456', '1234', '50', '654321'])
    def testTransfer(self, mockinputs):
        recipient_card = Card('654321', '4321', 200)
        recipient_user = User('Recipient User', '0987654321', '555-5556', recipient_card)
        self.allUser['654321'] = recipient_user
        
        with patch('builtins.input', side_effect=['123456', '1234', '50', '654321']):
            self.transaction.transfer()
            self.assertEqual(test_user.card.cardMoney, 50)
            self.assertEqual(recipient_user.card.cardMoney, 250)
            self.assertIsNotNone(recipient_user)
            self.assertIsNotNone(recipient_user.card)
            self.assertFalse(recipient_user.card.cardLock)

if __name__ == '__main__':
    unittest.main()