from flask import Flask, render_template, Blueprint, redirect, request
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)


# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books) 

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    books = book_repository.select_all()
    return render_template("books/new.html", new_book=books)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    genre = request.form["genre"]
    publisher = request.form["publisher"]
    author = request.form["author"]

    # select the user using the repository
    author = author_repository.select(author)
    # create a new book object
    book = Book(title, genre, publisher, author)
    # save that task object back to the db with the save method
    book_repository.save(book)

    return redirect('/books')

# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_task(id):
    book_repository.delete(id)
    return redirect("/books")

