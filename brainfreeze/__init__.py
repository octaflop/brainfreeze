from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola %s" % request.accept_mimetypes

if __name__ == "__main__":
    app.run(port=5000, debug=True)
