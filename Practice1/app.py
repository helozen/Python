from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "This is just for practice"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
