import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


@pytest.mark.parametrize('book_name', ['Harry Potter', 'The Lord of the Rings', 'SomeRandomName777'])
def test_add_new_book(book_name):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # проверяем, что книга присутствует в словаре books_genre
    assert book_name in collector.books_genre


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('It', 'Ужасы')
])
def test_set_book_genre_positive(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # проверяем, что книга присутствует в словаре books_genre
    assert book_name, genre in collector.books_genre


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('It', 'Ужасы')
])
def test_get_books_with_specific_genre_positive(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # создаем переменную genre_books, которая содержит список книг с жанрами,
    # если они соответствуют жанрам в списке genre
    genre_books = collector.get_books_with_specific_genre(genre)
    # проверяем, что название книги содержится в genre_books
    assert book_name in genre_books


@pytest.mark.parametrize('book_name, genre', [
    ("", "")
])
def test_set_book_genre_negative(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # проверяем, что книга c пустым названием и жанром не добавилась в словарь books_genre
    assert len(collector.books_genre) == 0


@pytest.mark.parametrize('book_name, genre', [
    ('Tarzan', 'Приключения'),
    ('Cinderella', 'Сказка')
])
def test_get_books_with_specific_genre_negative(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # создаем переменную fantasy_books,
    # которая содержит список книг, если жанр книги указан в переменной genre
    # жанр книг отсутствует в списке genre, поэтому книги не добавятся в books_with_specific_genre
    fantasy_books = collector.get_books_with_specific_genre(genre)
    # проверяем, что книги добавились в список fantasy_books
    assert book_name not in fantasy_books


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('Prostokvashino', 'Мультфильмы')
])
def test_get_books_for_children_positive(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # создаем переменную children_books,
    # которая содержит книги всех жанров, кроме ужасов и детективов
    children_books = collector.get_books_for_children()
    # проверяем, что книги добавились в список children_books
    assert book_name in children_books


@pytest.mark.parametrize('book_name, genre', [
    ('The Talented Mr. Ripley', 'Детективы'),
    ('Dracula', 'Ужасы'),
    ('It', 'Ужасы')
])
def test_get_books_for_children_negative(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # создаем переменную children_books,
    # которая должна содержать книги всех жанров, кроме ужасов и детективов
    children_books = collector.get_books_for_children()
    # используются значения жанров ужасы и детективы
    # проверяем, что эти книги не добавятся в список children_books
    assert book_name not in children_books


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('Prostokvashino', 'Мультфильмы')
])
def test_add_book_in_favorites(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # добавляем книгу в список favorites
    collector.add_book_in_favorites(book_name)
    # создаем переменную favorites, которая содержит список favorites
    favorites = collector.favorites
    # проверяем, что книга добавилась в список favorites
    assert book_name in favorites


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('Prostokvashino', 'Мультфильмы')
])
def test_delete_book_from_favorites(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # добавляем книгу в список favorites
    collector.add_book_in_favorites(book_name)
    # удаляем книгу из списка favorites
    collector.delete_book_from_favorites(book_name)
    # создаем переменную favorites, которая содержит все книги в списке favorites
    favorites = collector.favorites
    # проверяем, что после удаления книга отсутствует в списке favorites
    assert book_name not in favorites


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('Prostokvashino', 'Мультфильмы')
])
def test_get_list_of_favorites_books(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # добавляем книгу в список favorites
    collector.add_book_in_favorites(book_name)
    # создаем переменную favorites, в которую выводится возвращаемое значение get_list_of_favorites_books
    favorites = collector.get_list_of_favorites_books()
    assert book_name in favorites


@pytest.mark.parametrize('book_name', ['Harry Potter', 'The Lord of the Rings', 'Prostokvashino'])
def test_add_book_twice(book_name):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книги два раза
    collector.add_new_book(book_name)
    collector.add_new_book(book_name)
    # проверяем, что в список books_genre добавилось только одно значение
    assert len(collector.books_genre) == 1


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('Prostokvashino', 'Мультфильмы')
])
def test_get_book_genre(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # создаем переменную book_genre, в которую выводится возвращаемое значение get_book_genre
    book_genre = collector.get_book_genre(book_name)
    assert genre in book_genre


@pytest.mark.parametrize('book_name, genre', [
    ('Lucky Jim', 'Комедии'),
    ('The Lord of the Rings', 'Фантастика'),
    ('Prostokvashino', 'Мультфильмы')
])
def test_get_books_genre(book_name, genre):
    # создаем экземпляр (объект) класса BooksCollector
    collector = BooksCollector()

    # добавляем книгу
    collector.add_new_book(book_name)
    # добавляем жанр книги
    collector.set_book_genre(book_name, genre)
    # создаем переменную books_genre, в которую выводится возвращаемое значение get_books_genre
    books_genre = collector.get_books_genre()
    assert book_name, genre in books_genre
