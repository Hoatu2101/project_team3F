from flask import Flask, render_template

from Apartment_manage import dao

app = Flask(__name__,template_folder="template")
@app.route('/home')
def home_page():
    apartment = dao.load_apartment()
    return render_template('home.html',apartment=apartment)
@app.route("/index")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    print(dao.load_apartment())
    app.run(debug=True)
