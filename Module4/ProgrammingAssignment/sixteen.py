# Python V 3.11.1
# Used sqlite3 instead of sqlalchemy

import sqlite3 as sql

books = [
    ["The Weirdstone of Brisingamen", "Alan Garner", 1960],
    ["Perdido Street Station", "China Mieville", 2000],
    ["Thud!", "Terry Pratchett", 2005],
    ["The Spellman Files", "Lisa Lutz", 2007],
    ["Small Gods", "Terry Pratchett", 1992]
]

db = sql.connect("books.db")

if __name__ == "__main__":

    createQuery = "CREATE TABLE IF NOT EXISTS Books(Title TEXT, Author TEXT, Year INTEGER);"

    db.execute(createQuery)

    for b in books:
        insertQuery = "INSERT INTO Books(Title, Author, Year) VALUES(\"" + b[0] + "\", \"" + b[1] + "\", " + str(b[2]) + ");"
        db.execute(insertQuery)

    selectQuery = "SELECT title FROM Books WHERE 1 ORDER BY title ASC;"

    cursor = db.execute(selectQuery)
    for row in cursor:
        print(row)
