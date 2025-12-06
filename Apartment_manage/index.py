import json
import os
from flask import Flask, render_template, request
from Apartment_manage import dao

app = Flask(__name__, template_folder="template")

# Hàm đọc dữ liệu JSON
def read_json(filename):
    path = os.path.join(app.root_path, "template", "Data", filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Trang chính
@app.route("/index")
@app.route("/")
def index():
    notifications = read_json("notify.json")
    bills = read_json("pay.json")
    return render_template("index.html", notifications=notifications, bills=bills)


# Trang home với phân trang
@app.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    apartments, total_pages = dao.load_apartment_paginated(page=page, per_page=5)
    return render_template(
        "home.html",
        apartment=apartments,
        page=page,
        total_pages=total_pages
    )

# Trang liên hệ
@app.route("/lienhe")
def lienhe():
    return render_template("lienhe.html")

# Route tổng cho các extension
@app.route("/extension/<extension_name>")
def load_extension(extension_name):
    if extension_name == "notify_extension":
        notifications = read_json("notify.json")
        return render_template("extension/notify_extension.html", notifications=notifications)
    elif extension_name == "payment_extension":
        bills = read_json("pay.json")
        return render_template("extension/payment_extension.html", bills=bills)
    else:
        return render_template(f"extension/{extension_name}.html")

if __name__ == "__main__":
    app.run(debug=True)
