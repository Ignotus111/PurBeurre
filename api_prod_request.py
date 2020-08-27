import requests
import mysql.connector
import json
from constants import *

def requestprod():
    url = "https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux.json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers = headers, data = payload)
    json_prod = response.json()
    products_prod = json_prod.get('products')[:NB_PRODUCT]
    prod_name = [(data.get('product_name'),) for data in products_prod]
    prod_desc = [(data.get('generic_name'),) for data in products_prod]
    prod_url = [(data.get('url'),) for data in products_prod]
    prod_stores = [(data.get('stores'),) for data in products_prod]
    prod_code = [(data.get('id'),) for data in products_prod]
    prod_nutri = [(data.get('nutriscore_grade'),) for data in products_prod]
    prod_data = (prod_name, prod_desc, prod_url, prod_stores, prod_code, prod_nutri)
    sql = "INSERT INTO products (productname, description, offlink, store, barcode, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)"
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
    mycursor.executemany(sql, prod_data)
    connection.commit()
    mycursor.close()
requestprod()


"""
"INSERT INTO products" "(productname, description, offlink, store, barcode, nutritiongrade, bio)" "VALUES()"
"product_name" "generic_name" "url" "stores" "id" "nutriscore_grade"
"""
