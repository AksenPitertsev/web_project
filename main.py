from flask import *

app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template(
        "index.html",
        title=title,
        icon="https://icons.veryicon.com/png/Nature/Bumpy%20Planets/06%20mars.png",
    )
