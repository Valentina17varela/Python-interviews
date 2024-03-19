import unittest
from unittest.mock import patch

from src.reading_app import User, ReadingApp, Book


class TestReadingApp(unittest.TestCase):
    def setUp(self):
        self.user = User("test_user")
        self.app = ReadingApp()

    def test_add_book_to_library(self):
        book = Book("Test Book", "Test Author", 100)
        self.user.add_book_to_library(book)
        self.assertIn(book, self.user.library)

    def test_remove_book_from_library(self):
        book = Book("Test Book", "Test Author", 100)
        self.user.add_book_to_library(book)
        self.user.remove_book_from_library(book)
        self.assertNotIn(book, self.user.library)

    def test_set_active_book(self):
        book = Book("Test Book", "Test Author", 100)
        self.user.add_book_to_library(book)
        self.user.set_active_book(book)
        self.assertEqual(self.user.active_book, book)

    @patch("sys.stdout.write")
    def test_display_page(self, mock_stdout):
        self.app.register_user("test_user")
        book = Book("Test Book", "Test Author", 100)
        self.user.add_book_to_library(book)
        self.user.set_active_book(book)
        self.app.display_page("test_user")
        mock_stdout.assert_called_with("Page 1 of Test Book by Test Author")

    @patch("sys.stdout.write")
    def test_turn_page(self, mock_stdout):
        self.app.register_user("test_user")
        book = Book("Test Book", "Test Author", 100)
        self.user.add_book_to_library(book)
        self.user.set_active_book(book)
        self.app.turn_page("test_user")
        mock_stdout.assert_called_with("Turned to page 2")


if __name__ == "__main__":
    unittest.main()
