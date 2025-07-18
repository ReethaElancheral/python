from library import list_ebooks
print(list_ebooks())

from library import search_ebooks
results = search_ebooks('Python')
for book in results:
    print(book)

from library import read_all_ebooks
read_all_ebooks()
