from lesson15_HW.models import Tickets, Users
import datetime


def create_ticket(user):
    pass


def update_exchange_status_ticket(ticket_number: Tickets, user: Users):

    if Tickets.is_ticket_valid(ticket_uuid=ticket_number) == True:
        ticket_upd: Tickets = Tickets.get(Tickets.ticket_uuid == ticket_number)
        ticket_upd.is_available = False
        ticket_upd.user_id = user.user_uuid
        ticket_upd.status_change_dt = datetime.datetime.now()
        ticket_upd.save()
        if Users.is_exist(user.username) == True:
            user_upd: Users = Users.get(Users.username == user.username)
            user_upd.points += 20

            # user_upd.points = int(points_tmp) + 20
            user_upd.save()
            print('Вы успешно обменяли тикет на 20 поинтов')
            return "changed"
    else:
        return 'ticket was unavailable'


def exchange_ticket(user=None):
    ticket_number: str = ''
    while bool(ticket_number) == False:
        ticket_number = input("Тикет ").replace(' ', '')
        if ticket_number == 'exit':
            return 'exit'

    return update_exchange_status_ticket(ticket_number=ticket_number, user=Users.get(Users.username == 'tima1'))


if __name__ == "__main__":
    # user = Users.get(Users.user_uuid == 'bb51bb2b-1e14-4915-8114-58085b952c8f')
    # user = Users.get(Users.username == 'tima1')
    # print(user.email)
    # print(update_exchange_status_ticket(ticket_number='ebb94499-05c9-494f-9f4a-402c6543f244',
    #                                     user=Users.get(Users.username == 'tima1')))
    print(exchange_ticket())
