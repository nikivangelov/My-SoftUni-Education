book_name = input()
num_of_books = 0

while True:
    searching_book = input()

    if searching_book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {num_of_books} books.')
        break


    if searching_book == book_name:
        print(f'You checked {num_of_books} books and found it.')
        break
    num_of_books += 1
