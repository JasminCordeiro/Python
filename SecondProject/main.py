from flask import Flask, render_template 

app = Flask(__name__) #Esse arquivo atual representará minha aplicação da web.

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/budget")
def budget():
    return render_template("budget.html")

if __name__ == "__main__":
    app.run(debug=True)