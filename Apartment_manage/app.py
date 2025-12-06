from flask import Flask, render_template, request
import json, os

app = Flask(__name__)


# Load JSON
def load_apartments():
    json_path = os.path.join("Data", "apartment.json")
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)

with open("template/Data/apartment.json", "r", encoding="utf-8") as f:
    apartments = json.load(f)


# @app.route("/")
# def index():
#     apartments = load_apartments()
#
#     # Lọc tên
#     q = request.args.get("q", "")
#     if q:
#         apartments = [a for a in apartments if q.lower() in a["title"].lower()]
#
#     # Lọc giá
#     price_filter = request.args.get("price_filter", "")
#     if price_filter == "asc":
#         apartments = sorted(apartments, key=lambda x: float(x["price"].split()[0]))
#     elif price_filter == "desc":
#         apartments = sorted(apartments, key=lambda x: float(x["price"].split()[0]), reverse=True)
#
#     # Lọc diện tích
#     area_filter = request.args.get("area_filter", "")
#     if area_filter:
#         lo, hi = area_filter.split("-")
#         lo = int(lo)
#         hi = 999 if hi == "max" else int(hi)
#         apartments = [a for a in apartments if lo <= a["area"] <= hi]
#
#     return render_template("index.html", apartment=apartments)

    # # --- Phân trang ---
    # page = request.args.get("page", 1, type=int)  # Trang hiện tại
    # per_page = 4  # Mỗi trang 4 căn
    # total = len(apartments)  # Tổng số căn hộ
    # total_pages = math.ceil(total / per_page)
    #
    # # Tính vị trí slice
    # start = (page - 1) * per_page
    # end = start + per_page
    #
    # apartments_page = apartments[start:end]  # Lấy 4 căn mỗi trang
    #
    # return render_template(
    #     "index.html",
    #     apartment=apartments_page,
    #     page=page,
    #     total_pages=total_pages
    # )


if __name__ == "__main__":
    app.run(debug=True)
