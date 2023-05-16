library = {
        '1':{
        'author': 'Ole Kulet',
        'title': 'Rich dad poor dad',
        'year':2020,
        'ISBN': 10031
        }, 
        '2':{
        'author': 'Albert Einstein',
        'title': 'Thermodynamics',
        'year':2023,
        'ISBN': 10032
        },
        '3':{
        'author': 'Albert Einstein',
        'title': 'Thermodynamics',
        'year':2023,
        'ISBN': 10742
        },
        '4':{
        'author': 'Issac Newton',
        'title': 'The alchemy of happiness',
        'year':2023,
        'ISBN': 10451
        },
        '5':{
        'author': 'Bruce Lee',
        'title': 'Lost Memories',
        'year':2023,
        'ISBN': 10332
        },
        '6':{
        'author': 'Barack Obama',
        'title': 'Betrayal in the city',
        'year':2023,
        'ISBN': 34862
        },
        '7':{
        'author': 'Francis Imbuga',
        'title': 'Blossoms of the savannah',
        'year':2023,
        'ISBN': 10041
        },
        '8':{
        'author': 'Caucasian chalk circle',
        'title': 'Samson',
        'year':2023,
        'ISBN': 19032
        },

}
 
### In Python, show us how to: 
#Add a new book in the dictionary
# Retrieve a book based on Author 
# Find a books based on its ISBN number
# Update a title of the book
# Delete a certain book


# 1.Adding a new book in the dictionary
def add_book(author, title, year, isbn):
    new_book_id = str(len(library) + 1)
    new_book = {
        'author': author,
        'title': title,
        'year': year,
        'ISBN': isbn
    }
    library[new_book_id] = new_book
    print("Book added successfully.")

# 2.Retrieving a book based on Author 
def retrieve_book_by_author(author):
    found_books = []
    for book_id, book_details in library.items():
        if book_details['author'].lower() == author.lower():
            found_books.append(book_details)
    return found_books

# 3.Finding books based on its ISBN number
def find_book_by_isbn(isbn):
    for book_details in library.values():
        if book_details['ISBN'] == isbn:
            return book_details
    return None

# 4.Updating a title of the book
def update_book_title(book_id, new_title):
    if book_id in library:
        library[book_id]['title'] = new_title
        print("Title updated successfully.")
    else:
        print("Book not found.")

# 5.Deleting a certain book
def delete_book(book_id):
    if book_id in library:
        del library[book_id]
        print("Book deleted successfully.")
    else:
        print("Book not found.")

# examples:

# 1.Adding a new book in the dictionary
# add_book("Bertolt bretch", "The river and the source", 1997, 12345)
# print(library)

# 2.Retrieving a book based on Author 
# books_by_author = retrieve_book_by_author("Albert Einstein")
# print(books_by_author)

# 3.Finding books based on its ISBN number
# book_by_isbn = find_book_by_isbn(10032)
# print(book_by_isbn)

# 4.Updating a title of the book
# update_book_title('2', 'New Title')
# print(library)

# 5.Deleting a certain book
# delete_book('3')
# print(library)