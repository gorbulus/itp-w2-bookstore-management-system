def create_bookstore(name):
    '''Creating a dictionary and returning in one line'''
    return {
        "name" : name,
        "authors" : [],
        "books" : [],
    }
    
    
def get_bookstore_name(bookstore):
    return bookstore["name"]


def add_author(bookstore, name, nationality):
    '''Bookstore has to be passed here to store the name of the author (see tests)'''
    author = {
        "name" : name,
        "nationality" : nationality
    }
    '''Appending a list "authors" inside of the bookstore dictionary'''
    bookstore["authors"].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore["authors"]:
        if author["name"] == name:
            return author


def add_book(bookstore, title, isbn, author):
    book = {
        "title" : title,
        "isbn" : isbn,
        "author" : author
    }
    bookstore["books"].append(book)
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore["books"]:
        if book["title"] == title:
            return book


def get_books_by_author(bookstore, author):
    books = []
    for book in bookstore["books"]:
        if book["author"] == author:
            books.append(book)
    return books

'''All tests passed at this point'''
