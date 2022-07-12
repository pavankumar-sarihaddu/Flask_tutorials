from flask import Flask, redirect, url_for, render_template,

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("menupage.html")

@app.route("/login", methods=["POST","GET"])
def login():
 
    return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"{usr}"

if __name__ == "__main__":
    app.run(debug=True)