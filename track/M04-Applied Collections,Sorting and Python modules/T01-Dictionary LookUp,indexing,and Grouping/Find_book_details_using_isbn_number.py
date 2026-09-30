def find_book(books, isbn):
    if isbn in books:
        return books[isbn]
    return None

books ={

"97801":{"title": "Clean Code", "author": "Robert Martin"},

"97802":{"title": "Python Crash Course", "author": "Eric Matthes"},

"97883":{"title": "The Pragmatic Programmer", "author": "Andrew Hunt"},

"97884": {"title": "Algorithms", "author": "Robert Sedgewick"}

}

isbn=input()

book =find_book(books, isbn)

if book is None:
    print("Book not found")

else:
    print(book["title"])
    print(book ["author"])