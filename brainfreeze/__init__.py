import sys
# Static flask imports
from flask import Flask, render_template
# Dynamic flask imports
from flask import request
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route("/")
def index():
    # return "Hola %s" % request.accept_mimetypes
    return render_template("index.html", page=page)

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path).html
    return render_template("page.html", page=page)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    app.run(port=5000, debug=DEBUG)
