import unittest
from unittest.mock import patch
from admin.view import AdminView
from admin.store import Store
from admin.action import action
from admin.card import User, Card

import time 


class TestAdminView(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up the test class")

    def setUp(self):
        self.admin_view_instance = AdminView(run=False)
        

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class")

   
    def test_login_credentials(self):
        with patch('builtins.input', side_effect=['1', '1']):
            result = self.admin_view_instance.login()            
            self.assertTrue(result)
            
            self.assertNotIn('1', self.admin_view_instance.users)
            #user = self.admin_view_instance.users['1']
            # self.assertEqual(user.phone, '7890123456')
            # self.assertEqual(user.idCard, '123456')
            
        with patch('builtins.input', side_effect=['1', '2']):
            result = self.admin_view_instance.login()            
            self.assertFalse(result)
            
        with patch('builtins.input', side_effect=['3', '2']):
            result = self.admin_view_instance.login()            
            self.assertFalse(result)
            

    def test_admin_view_option(self):
        
        with patch('builtins.input', side_effect=['2', '2']):
            result = self.admin_view_instance.login()
        self.assertFalse(result)  
#        self.assertEqual(self.admin_view_instance.login_attempts, 3) 
#        self.assertIsNone(self.admin_view_instance.users)
        
        
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
