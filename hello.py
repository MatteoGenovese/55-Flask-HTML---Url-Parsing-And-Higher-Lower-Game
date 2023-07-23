from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return f"<p>Hello, world!</p>" \
           f"<img src='https://staticgeopop.akamaized.net/wp-content/uploads/sites/32/2022/10/GEOPOP-THUMB-ARTICOLO.jpg'>"


@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello {name}!</p>"


if __name__ == "__main__":
    app.run(debug=True)
