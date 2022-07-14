from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    return render_template("index.html", some_text=some_text, current_year=current_year)

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/test")
def test():
    return render_template("base.html")



if __name__ == '__main__':
    app.run(port="443", use_reloader=True) 