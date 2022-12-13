import uuid

import peewee
import random

from ne_magazin.models import Products, Users, Orders

def create_default_product(number:int=None):
    for i in range(number):
        rd, rc, cost = random.randint(1,1400), random.randint(1,1400), random.randint(1,10000)

        create_default_product: Products = Products.create(product_uuid=uuid.uuid4(), name=f'product {rd}_{rc}', cost=int(f"{cost}"), count=int(f'{rd}'))
    return create_default_product

def list_of_products():
    products_list: peewee.Model = Products.select()
    return [product for product in products_list]
    # print([it for it in products_list])


def render_list(products: list[Products]):
    print(
        f"""
 UUID \t\t\t\t\t\t\t            Стоимость \t\t\t Кол-во \t\t Название
==========================================================================================================""")
    for item in products:
        print(
            f""" {str(item.product_uuid):<40}\t\t{item.cost:<16} {item.count:<4} \t\t\t {item.name} """)
    print()



def products_list_view():
    render_list(list_of_products())
    while True:
        choice = input("Send any char to return back: ").replace(" ", '')
        if bool(choice) is True:
            return False


if __name__ == "__main__":
    # create_default_product(5)
    # a = render_list(list_of_products())
    # print(a)
    # pass
    products_list_view()