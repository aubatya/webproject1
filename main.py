from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/<item>")
def show_item_profile(item):
    item = escape(item)
    return render_template(item)

if __name__ == "__main__":
    app.run(debug = True)