from flask import Flask, render_template
from controllers.books_controller import books_blueprint

# TODO: import books blueprint here

app = Flask(__name__)

# TODO: register books blueprint here

app.register_blueprint(books_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
