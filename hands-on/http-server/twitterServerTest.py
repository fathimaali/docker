import unittest

# Assuming your Flask app is named 'app'
from twitterServer import userExistsCheckInternal

class TestUserExistsCheckInternal(unittest.TestCase):

    def setUp(self):
        users = {
            1: {'username': 'fat'},
            2: {'username': 'haf'},
            3: {'username': 'ali'}
        }
        
        result = userExistsCheckInternal('fat')
        self.assertTrue(result)

    def test_user_does_not_exist(self):
        users = {
            1: {'username': 'user1'},
            2: {'username': 'user2'},
            3: {'username': 'user3'}
        }
        
        result = userExistsCheckInternal('nonexistent_user')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()