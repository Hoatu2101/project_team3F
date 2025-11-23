import json


def load_apartment():
    with open("template/Data/apartment.json",encoding="utf-8") as f:
        return json.load(f)
if __name__ == "__main__":
    print(load_apartment())