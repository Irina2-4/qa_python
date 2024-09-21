import pytest

from main import BooksCollector
class TestBooksCollector:
    @pytest.mark.parametrize(
        'book',
        [
            'Чемодан',
            'Компромис',
            'Наши',
            'Иностранка'
        ]
    )
    def test_add_new_book_add_books_pozitive(self,book):
        collector = BooksCollector()
        sum = len(collector.get_books_genre())
        for i in range(4):
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == sum + 1
    @pytest.mark.parametrize(
        'book',
        [
            '',
            'Жизнь,необыкновенные и удивительные приключения Робинзона Крузо'
        ]
    )
    def test_add_new_book_add_long_name_negative(self,book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_two_books_negative(self):
        collector = BooksCollector()
        collector.add_new_book('Дюймовочка')
        collector.add_new_book('Дюймовочка')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_add_pozitive(self):
        book = 'Трое из Простоквашино'
        genre = 'Мультфильмы'
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book,genre)
        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_pozitive(self):
        collector = BooksCollector()
        book = 'Волкодав'
        genre = 'Фантастика'
        collector.add_new_book(book)
        collector.set_book_genre(book,genre)
        assert collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre_pozitive(self):
        collector = BooksCollector()
        book = 'Страна призраков'
        genre = 'Ужасы'
        collector.add_new_book(book)
        collector.set_book_genre(book,genre)
        assert collector.get_books_with_specific_genre(genre) == [book]

    def test_get_books_for_children_pozitive(self):
        collector = BooksCollector()
        book = 'Золушка'
        genre = 'Мультфильмы'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        list_for_children = []
        for name,genre in collector.get_books_genre().items():
            if genre not in collector.genre_age_rating and genre in collector.genre:
                list_for_children.append(book)
        assert collector.get_books_for_children() == list_for_children

    def test_add_book_in_favorites_pozitive(self):
        collector = BooksCollector()
        book = 'Полианна'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()
    def test_delete_book_from_favorites_pozitive(self):
        collector = BooksCollector()
        book = 'Микки Маус'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()