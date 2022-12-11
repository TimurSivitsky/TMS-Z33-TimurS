import uuid

import peewee

from models import Products, Users, Orders


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


def choose_product():
    product_uuid: str = ''
    try:
        while bool(product_uuid) == False:
            product_uuid, *count = map(str, input(" Купить > ").split())
            if product_uuid == 'exit':
                return 'exit'
        return product_uuid, int(count[0])
    except ValueError:
        print(product_uuid)
        return product_uuid, 1

    except IndexError:
        print(product_uuid)
        return product_uuid, 1



def make_order(order: tuple, user: Users):
    if len(order) == 2:
        product_id: Products = order[0]
        count: int = order[1]
        print(f" dfaasdf product_id: {product_id}, count: {count}")

        try:
            order: Orders = Orders.create(order_uuid=uuid.uuid4(), user_id=user.user_uuid,
                                          product_id=product_id, count=count)
            product_upd: Products = Products.get(Products.product_uuid == product_id)
            product_upd.count -= count
            product_upd.save()

            user_upd: Users = Users.get(Users.user_uuid == user.user_uuid)
            user_upd.points += 7
            user_upd.save()
            return order
        except:
            print('something went wrong')


    elif len(order) < 2:
        print(order)
        return 'exit'
    # print(f" dfaasdf product_id: {product_id}, count: {count}")




if __name__ == "__main__":
    user = Users.get(Users.username == 'tima1')

    render_list(list_of_products())

    ass=choose_product()
    print(ass)

    make_order(ass, user)

    render_list(list_of_products())
    # print(exchange_ticket(user=Users.get(Users.username == 'tima1')))
    # a:Products = list_of_products()
    # choose_product(render_list(list_of_products()))
    # for i in a:
    #     print(i.name, i.cost, i.count, i.product_uuid)
