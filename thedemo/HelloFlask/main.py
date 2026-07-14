from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<h1 style='Bold'>"
            "<center>Hello, World!</center>"
            "</h1>")

@app.route("/username/<name>")
def username(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)