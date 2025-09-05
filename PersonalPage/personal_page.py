from flask import Flask,url_for,render_template, request,redirect
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" ,personal_name = "Kaloyan Hristov")

@app.route("/about")
def about():
    text = """
       Hello my name is Kaloyan Hristov and I am born in Sofia,Bulgaria <br> since I was very young i had passion about programming <br>and currently Im learning about Flask so this is <br>a small project in Flask called 'Personal Page'.
    """
    return render_template("about.html", about_me = text)

@app.route("/contact", methods = ["GET","POST"])
def contact():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        message = request.form["message"]
        print(f"Received message from {username} ({email}{message})")
        print("I'll contact you soon!")
        #👉 „След като обработя нещо (например форма), върни потребителя обратно на началната страница.“
        return redirect(url_for("index"))
    #Защо има двете реда заедно в един route?
    # Защото зависи какъв е методът на заявката:
    # Ако е POST → вече си получил данни от формата → обикновено искаш да пренасочиш потребителя (redirect), за да няма повторно изпращане на формата при refresh.
    # Ако е GET → просто показваш формата с render_template("contact.html").
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)