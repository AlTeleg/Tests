import unittest
import accounting
from unittest.mock import patch


class AccountingTests(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_check_document_existance_pos(self):
        user_doc_number = "2207 876234"
        result = accounting.check_document_existance(user_doc_number)
        self.assertEqual(result, True)
    def test_check_document_existance_neg(self):
        user_doc_number = "55 23425"
        result = accounting.check_document_existance(user_doc_number)
        self.assertEqual(result, False)

    @patch('builtins.input', "2207 876234")
    def test_get_doc_owner_name_pos(self):
        pass

    @patch('builtins.input', "55 23425")
    def test_get_doc_owner_name_neg(self):
        pass

    def test_get_all_doc_owners_names(self):
        pass
    def test_add_new_shelf(self):
        pass
    def test_append_doc_to_shelf(self):
        pass
    def test_delete_doc(self):
        pass
    def test_get_doc_shelf(self):
        pass
    def test_move_doc_to_shelf(self):
        pass
    def test_show_document_info(self):
        pass
    def test_show_all_docs_info(self):
        pass

    @patch('builtins.input', side_effect=["2207 876234", "passport", "Василий Гупкин", 3])
    def test_add_new_doc(self, mock_input):
        accounting.add_new_doc()


if __name__ == '__main__':
    unittest.main()

