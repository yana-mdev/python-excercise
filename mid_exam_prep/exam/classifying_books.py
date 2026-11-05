def classify_books(*args, **kwargs):
    fiction_books = {}
    nonfiction_books = {}

    for genre, book_title in args:
        if genre == "fiction":
            fiction_books[book_title] = 0
        else:
            nonfiction_books[book_title] = 0

    for ISBN, book_title in kwargs.items():
        if book_title in fiction_books:
            fiction_books[book_title] = ISBN
        elif book_title in nonfiction_books:
            nonfiction_books[book_title] = ISBN

    result = []

    sorted_fiction_books = sorted(fiction_books.items(), key=lambda x: x[1])
    sorted_nonfiction_books = sorted(nonfiction_books.items(), key=lambda x: x[1], reverse=True)

    if sorted_fiction_books:
        result.append("Fiction Books:")
        for book_title, ISBN in sorted_fiction_books:
            result.append(f"~~~{ISBN}#{book_title}")

    if sorted_nonfiction_books:
        result.append("Non-Fiction Books:")
        for book_title, ISBN in sorted_nonfiction_books:
            result.append(f"***{ISBN}#{book_title}")

    return "\n".join(result)