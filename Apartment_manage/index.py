from flask import Flask, render_template

from Apartment_manage import dao

app = Flask(__name__,template_folder="template")
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/home')
def home_page():
    apartment = dao.load_apartment()
    return render_template('home.html',apartment=apartment)
@app.route("/index")
def load_extensions():
    return render_template("index.html")
@app.route("/extension/payment_extension")
@app.route("/extension/<extension_name>")
def load_extension(extension_name="payment_extension"):
    return render_template(f"extension/{extension_name}.html")
if __name__ == "__main__":
    print(dao.load_apartment())
    app.run(debug=True)
