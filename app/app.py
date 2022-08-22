from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "get return"
    elif request.method == "POST":
        return "post return", 201

@app.route('/teste')
def index_test():
    return "nova rota"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)