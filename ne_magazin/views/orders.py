import uuid

import peewee

from ne_magazin.models import Products, Users, Orders


def list_of_products():
    products_list: peewee.Model = Products.select()
    return [product for product in products_list]
    # print([it for it in products_list])


def render_list(products: list[Products]):
    print(
        f"""
 UUID \t\t\t\t\t\t\t\t            Стоимость \t\t Кол-во \t\t Название
==========================================================================================================""")
    for item in products:
        print(
            f""" {item.product_uuid}\t\t\t{item.cost} \t\t\t  {item.count} \t\t\t {item.name} """)
    print()

# @render_list(list_of_products())
def choose_product():
    render_list(list_of_products())
    while True:
        try:
            product_uuid, *count = map(str, input(" Купить > ").split())

            if uuid.UUID(product_uuid) and int(count[0]):
                Products.is_exist(product_uuid)
                # current_product:Products = Products.get(Products.product_uuid == product_uuid)
                return Products.get(Products.product_uuid == product_uuid), int(count[0])

            else:
                rtry = input('Wrong productID or unavailable ticket \nWill your try again(Y|N): ')
                match rtry.lower():
                    case 'y': pass
                    case 'n': return False
                    case _: pass
        except (ValueError, IndexError, Products.DoesNotExist) as exception:
            print(f" Error: {exception}")
            rtry = input('Wrong productID or unavailable ticket \nWill your try again(Y|N): ')
            match rtry.lower():
                case 'y': pass
                case 'n': return False
                case _: pass

def create_order(product: Products, count: int, username: str):
    current_user: Users = Users.get(Users.username==username)
    try:
        new_order: Orders = Orders.create(order_uuid=uuid.uuid4(), user_id=current_user.user_uuid,
                                      product_id=product.product_uuid, count=count)
        product_upd: Products = Products.get(Products.product_uuid == product.product_uuid)
        product_upd.count -= count
        product_upd.save()

        current_user.points += 7
        current_user.save()
        return new_order

    except Exception as e:
        print(f'something went wrong in CREATTION ORDER {e}')


def laucnh_order_view(username):
    while True:
        try:

            current_product, count = choose_product()
            return create_order(current_product, count, username=username)
        except TypeError:
            return False


if __name__ == "__main__":
    #
    # a:Products = choose_product().name
    # create_order()
    # print(a)
    #
    # current_product, count = choose_product()
    # print(create_order(current_product, count, 'ihar'))
    laucnh_order_view()