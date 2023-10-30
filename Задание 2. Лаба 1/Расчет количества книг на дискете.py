# TODO Найдите количество книг, которое можно разместить на дискете
from typing import Tuple
diskette_size = 1.44
page_count = 100
lines = 50
symbols_per_line = 25
bytes_for_sym = 4
book_size = page_count * lines * symbols_per_line * bytes_for_sym
book_size_mb = book_size / (1024 * 1024)
books_on_diskette = diskette_size / book_size_mb
print("Количество книг, помещающихся на дискету:", int(books_on_diskette))
