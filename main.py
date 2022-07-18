from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)



@app.route("/")
def index():
    some_t = "Message from the handler."
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    return render_template("index.html", some_text=some_t, current_year=current_year, cities=cities)

@app.route("/about",  methods=["GET", "POST"])
def about_me():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    else:
        return render_template("about.html")

@app.route("/test")
def test():
    return render_template("base.html")

@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_name)
    print(contact_message)

    lista_about=[contact_name, contact_name, contact_message]

    response = make_response(render_template("success.html"))
    response.set_cookie("user_name", contact_name)


    return render_template("success.html", lista_about=lista_about)

if __name__ == '__main__':
    app.run(port="443", use_reloader=True) 