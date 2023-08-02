import json
import requests

categories_slug = []
categories_raw = requests.get('https://api.technodom.kz/menu/api/v1/menu/breadcrumbs/categories/smartfony?brands=samsung').json()
for category in categories_raw:
    categories_slug.append(category["category_code"])

products = []
for category_slug in categories_slug:
    try:
        products_raw = requests.get(
            'https://api.technodom.kz/katalog/api/v1/products/category/' + category_slug + '?city_id=5f5f1e3b4c8a49e692fefd70&limit=24&brands=samsung&sorting=score&price=0'
        ).json()
        for product_raw in products_raw["payload"]:
            products.append({
                "title": product_raw["title"],
                "price": product_raw["price"]
            })
    except:
        pass

products = list({product["title"]: product for product in products}.values())

with open('products.json', 'w', encoding='utf-8') as outfile:
    json.dump(products, outfile, indent=2, ensure_ascii=False)