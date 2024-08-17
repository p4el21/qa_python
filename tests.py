import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
# Добавление 2 книг
    def test_add_new_book_two_books(self):
        collector = BooksCollector()     # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Гордость и предубеждение и зомби')    # добавляем две книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
        print('\nТест пройден!')

#Добавление одной книги
    def test_add_new_book_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.books_genre
        print('\nТест пройден!')

#Добавление существующей книги
    def test_add_new_book_add_existing_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Гордость и предубеждение и зомби': 'Ужасы'}
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1 and collector.books_genre['Гордость и предубеждение и зомби']
        print('\nТест пройден!')

#Добавление книг с разрешенной длинной символов
    @pytest.mark.parametrize('name', ['Я', 'Король Артур', 'Гордость и предубеждение и зомби фиксики'])
    def test_add_new_book_valid_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre
        print('\nТест пройден!')

 # Добавление книг с неразрешенной длинной символов
    @pytest.mark.parametrize('name', ['', 'Гордость и предубеждение и зомби товарищи'])
    def test_add_new_book_invalid_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre
        print('\nТест пройден!')

#Изменение жанра книги
    def test_set_book_genre_change_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Гордость и предубеждение и зомби': 'Ужасы'}
        new_genre = 'Фантастика'
        collector.set_book_genre('Гордость и предубеждение и зомби', new_genre)
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == new_genre
        print('\nТест пройден!')

#Просмотр жанра книги
    def test_get_book_genre_book_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Гордость и предубеждение и зомби': 'Ужасы'}
        assert collector.get_book_genre('Гордость и предубеждение и зомби')
        print('\nТест пройден!')

#Просмотр книг с жанром "Комедии"
    def test_get_books_with_comedy_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Гордость и предубеждение и зомби': 'Ужасы',
                                 'Печенеги и половцы': 'Комедии',
                                 'Отцы и молодцы': 'Мультфильмы',
                                 'Добрый вечер я Бен Флетчер': 'Комедии',
                                 'Криминальное пиво': 'Детективы',
                                 'Светлый мир': 'Фантастика'}
        genre = collector.get_books_with_specific_genre('Комедии')
        assert len(genre) == 2
        print('\nТест пройден!')

#Просмотр словаря
    def test_get_books_genre_view_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Печенеги и половцы')
        collector.add_new_book('Отцы и молодцы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Печенеги и половцы', 'Комедии')
        collector.set_book_genre('Отцы и молодцы', 'Мультфильмы')
        expected_result = {
        'Гордость и предубеждение и зомби': 'Ужасы',
        'Печенеги и половцы': 'Комедии',
        'Отцы и молодцы': 'Мультфильмы'}
        result = collector.get_books_genre()
        assert result == expected_result
        print('\nТест пройден!')

#Просмотр книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.books_genre = {'Гордость и предубеждение и зомби': 'Ужасы',
                                 'Печенеги и половцы': 'Комедии',
                                 'Отцы и молодцы': 'Мультфильмы',
                                 'Добрый вечер я Бен Флетчер': 'Комедии',
                                 'Криминальное пиво': 'Детективы',
                                 'Светлый мир': 'Фантастика'}
        children_books = collector.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' not in children_books
        assert 'Криминальное пиво' not in children_books
        assert 'Печенеги и половцы' in children_books
        assert 'Отцы и молодцы' in children_books
        assert 'Добрый вечер я Бен Флетчер' in children_books
        assert 'Светлый мир' in children_books
        print('\nТест пройден!')

#Добавление книги в избранное
    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites
        print('\nТест пройден!')

#Удаление книги из избранного
    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.favorites
        print('\nТест пройден!')

#Вывод избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Печенеги и половцы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites = collector.get_list_of_favorites_books()
        assert favorites
        print('\nТест пройден!')
