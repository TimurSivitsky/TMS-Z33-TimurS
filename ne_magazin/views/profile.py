from ne_magazin.models import *


def profile_view(username):

    user: Users = Users.get(Users.username == username)
    try:
        user_orders: Orders = Orders.select().where(Orders.user_id == user.user_uuid)
        user_tickets: Tickets = Tickets.select().where(Tickets.user_id == user.user_uuid)
    except Exception as e:
        print(e)

    print(user)
    print("Used Tickets")
    for tickets in user_tickets:
        print(tickets)
    print("Orders")
    for orders in user_orders:
        print(orders)

    while True:
        choice = input("Send any char to return back: ").replace(" ", '')
        if bool(choice) is True:
            return False

# profile_view('tima')
