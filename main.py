from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/test")
def test():
    return render_template("base.html")



if __name__ == '__main__':
    app.run(port="443", use_reloader=True) 