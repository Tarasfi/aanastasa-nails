import json
def json_to_db():
    with open('../data/price.json', encoding='utf-8') as p:
        prices = json.load(p)

    for item in prices:
        title = item.get("title", "No title")
        price = item.get("price")
        variants = item.get("variants")

        if price:
            print(f" {title},  {price}")
        elif variants:
            print(f"{title}:")
            for variant in variants:
                length = variant.get("length", "Unknown length")
                var_price = variant.get("price", "Unknown price")
                print(f"  - {length}: {var_price}")
        else:
            print(f"{title}: No price or variants found")

json_to_db()


