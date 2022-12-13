from ne_magazin.models import *


def profile_view(username):

    user: Users = Users.get(Users.username == username)
    try:
        user_orders: Orders = Orders.select().where(Orders.user_id == user.user_uuid)
        user_tickets: Tickets = Tickets.select().where(Tickets.user_id == user.user_uuid)
    except Exception as e:
        print(e)

    print(user)
    print("\nUsed Tickets: ", end=' ')
    if user_tickets:
        for tickets in user_tickets:
            print(tickets)
    else: print(None)

    print("\nOrders: ", end=' ')
    if user_orders:
        for orders in user_orders:
            print(orders)
    else: print(None)

    while True:
        choice = input("Send any char to return back: ").replace(" ", '')
        if bool(choice) is True:
            return False

# profile_view('tima')
