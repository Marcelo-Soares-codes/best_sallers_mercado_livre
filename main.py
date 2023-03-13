import requests
import os


url = "https://api.mercadolibre.com/sites/MLB/"
url_01 = "https://api.mercadolibre.com/sites/MLB/search?category=MLB1051&sort=sold_quantity_desc"

def choose_category():
    response = requests.get(url+"categories")
    print("-------- SELECIONE A CATEGORIA --------")
    categories = []
    for num, category in enumerate(response.json()):
        categories.append(category)
        print(f"{num}. {category['name']}")
    num = input("DIGITE O NUMERO ATRIBUIDO: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    return categories[int(num)]

def best_sellers(category):

    response = requests.get(url+"search?category="+category["id"]+"&sort=sold_quantity_desc")
    print("-------- PRODUTOS MAIS VENDIDOS --------")
    for num, product in enumerate(response.json()['results']):
        print(f"{num}. {product['title']}")

category = choose_category()
best_sellers(category)