import pytest

from src.reading_app import User, ReadingApp, Book


@pytest.fixture
def user():
    return User("test_user")


@pytest.fixture
def app():
    return ReadingApp()


def test_add_book_to_library(user):
    book = Book("Test Book", "Test Author", 100)
    user.add_book_to_library(book)
    assert book in user.library


def test_remove_book_from_library(user):
    book = Book("Test Book", "Test Author", 100)
    user.add_book_to_library(book)
    user.remove_book_from_library(book)
    assert book not in user.library


def test_set_active_book(user):
    book = Book("Test Book", "Test Author", 100)
    user.add_book_to_library(book)
    user.set_active_book(book)
    assert user.active_book == book


def test_display_page(capsys, user, app):
    app.register_user("test_user")
    book = Book("Test Book", "Test Author", 100)
    user_test = app.users["test_user"]
    user_test.add_book_to_library(book)
    user_test.set_active_book(book)
    app.display_page("test_user")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Page 1 of Test Book by Test Author"


def test_turn_page(capsys, user, app):
    app.register_user("test_user")
    book = Book("Test Book", "Test Author", 100)
    user_test = app.users["test_user"]
    user_test.add_book_to_library(book)
    user_test.set_active_book(book)
    app.turn_page("test_user")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Turned to page 2"
