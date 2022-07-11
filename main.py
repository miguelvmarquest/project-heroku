from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello/test/smartninja")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/test")
def test():
    return "Test ;) http://127.0.0.1:30000/about"



if __name__ == '__main__':
    app.run(port="30000", use_reloader=True) 