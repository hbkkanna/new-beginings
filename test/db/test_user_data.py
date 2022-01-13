import unittest
from db import user_data
from common.util import create_user_reference

user = {
    "username": "Kannan Muthu",
    "dob": "March 15 1982",
    "address": "28 Roberts Road Exeter Ex2 4HD",
    "phone": "+447404384179"
}

user2 = {
    "username": "Muthu Test",
    "dob": "March 15 1982",
    "address": "28 Roberts Road Exeter Ex2 4HD",
    "phone": "+447404384179"
}

updated_user = {
    "username": "Kannan Muthu",
    "dob": "March 15 1982",
    "address": "28 Roberts Road Exeter Ex2 4HD",
    "phone": "+16692463727"
}


class DBTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_user(self):
        user_id = create_user_reference();
        user_data.create_user(user_id, user)
        self.assertEqual(user_data.get_user(user_id), user)

    def test_update_user(self):
        print("update user")
        user_id = create_user_reference();
        user_data.create_user(user_id, user);
        user_data.update_user(user_id, updated_user)
        self.assertEqual(user_data.get_user(user_id), updated_user)
        print(user_data.db)

    def test_delete_user(self):
        user_id = create_user_reference();
        user_data.create_user(user_id, user);
        user_data.delete_user(user_id)
        self.assertEqual(user_data.get_user(user_id), None)

    def test_check_duplicate(self):
        user_data.db.update({"TT-12121":user, "SS-34343":user2})
        print(user_data.check_duplicate(user))



    def tearDown(self):
        user_data.db.clear()


if __name__ == '__main__':
    unittest.main()
