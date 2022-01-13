import unittest
from common.util import create_user_reference, validate_user

class UtilTest(unittest.TestCase):
    def test_create_user_reference(self):
        ref = create_user_reference()
        self.assertTrue(len(ref)>3)

    def test_validate_user(self):
        self.assertTrue(validate_user("Kannan"))
        self.assertFalse(validate_user("kad"))

if __name__ == '__main__':
    unittest.main()
