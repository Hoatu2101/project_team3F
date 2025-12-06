import json


def load_apartment():
    with open("template/Data/apartment.json",encoding="utf-8") as f:
        return json.load(f)

def load_apartment_paginated(page=1, per_page=5):
    apartments = load_apartment()
    total = len(apartments)

    # Tính index bắt đầu và kết thúc
    start = (page - 1) * per_page
    end = start + per_page

    # Lấy 5 căn dựa vào trang
    apartments_page = apartments[start:end]

    # Tính tổng số trang
    total_pages = (total + per_page - 1) // per_page

    return apartments_page, total_pages

if __name__ == "__main__":
    print(load_apartment())