# Python V 3.11.1

from flask import Flask, request
import json

app = Flask(__name__)

class Books():
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

    def __repr__(self):
        return f"{self.book_name} is by {self.author}"

books = []



with open("books.json", "r") as fromFile:
        for i in fromFile:
            books.append(Books(json.loads(i)["id"], json.loads(i)["book_name"], json.loads(i)["author"], json.loads(i)["publisher"]))

@app.route("/")
def index():
    return "Hello"

@app.route("/books")
def get_books():

    for b in books:
        yield json.dumps({"id": b.id, "book_name": b.book_name, "author": b.author, "publisher": b.publisher})

@app.route("/books/<id>")
def get_book_by_id(id):
    for b in books:
        if str(b.id) == str(id):
            return json.dumps({"id": b.id, "book_name": b.book_name, "author": b.author, "publisher": b.publisher})

@app.route("/books", methods=["POST"])
def add_book():
    request.get_json(force=True)
    book = Books(request.json["id"], request.json["book_name"], request.json["author"], request.json["publisher"])
    books.append(book)
    with open("books.json", "w") as toFile:
        for b in books:
            toFile.write(json.dumps({"id": b.id, "book_name": b.book_name, "author": b.author, "publisher": b.publisher}) + "\n")

    return {"id": book.id}

@app.route("/books/<id>", methods=["DELETE"])
def delete_book(id):
    
    for b in books:
        if str(b.id) == str(id):
            books.remove(b)

    with open("books.json", "w") as toFile:
        for b in books:
            toFile.write(json.dumps({"id": b.id, "book_name": b.book_name, "author": b.author, "publisher": b.publisher}) + "\n")

    return f"{id} was deleted"

    
