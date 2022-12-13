import uuid

from ne_magazin.models import Tickets, Users
import datetime
import random


def create_default_tickets(number):
    for _ in range(number):
        default_ticket: Tickets = Tickets.create(ticket_uuid=uuid.uuid4(), is_available=True)
    return True


def update_exchange_status_ticket(ticket_number: Tickets, username: str, user_uuid: str):
    if Tickets.is_ticket_valid(ticket_uuid=ticket_number) == True:
        ticket_upd: Tickets = Tickets.get(Tickets.ticket_uuid == ticket_number)
        ticket_upd.is_available = False
        if Users.is_exist(username) == True:
            user_upd: Users = Users.get(Users.username == username)
            ticket_upd.user_id = user_uuid
            ticket_upd.status_change_dt = datetime.datetime.now()
            ticket_upd.save()

            user_upd.points += 20
            user_upd.save()
            print('Вы успешно обменяли тикет на 20 поинтов')
            return True
        else:
            print(f'User {username} is not exists')
            return False

    else:
        print(f"Ticket {ticket_number} is not available")
        return False


def exchange_ticket(username, user_uuid):
    ticket_number: str = ''
    # while bool(ticket_number) == False:
    #     ticket_number = input("Тикет ").replace(' ', '')
    #     if ticket_number == 'exit':
    #         return 'exit'
    while True:
        ticket_number = input("Тикет ").replace(' ', '')
        is_ticket = Tickets.is_ticket_valid(ticket_number)
        if bool(ticket_number) == True:
            if is_ticket == True:
                return update_exchange_status_ticket(ticket_number=ticket_number, username=username, user_uuid=user_uuid)
            elif is_ticket == False:
                rtry = input('Wrong ticket_id or unavailable ticket \nWill your try again(Y|N): ')
                match rtry.lower():
                    case 'y':
                        pass
                    case 'n':
                        return False
                    case _:
                        pass
        else:
            rtry = input('Wrong ticket_id or unavailable ticket \nWill your try again(Y|N): ')
            match rtry.lower():
                case 'y':
                    pass
                case 'n':
                    return False
                case _:
                    pass




    # return update_exchange_status_ticket(ticket_number=ticket_number, username=username, user_uuid=user_uuid)


if __name__ == "__main__":
    # user = Users.get(Users.user_uuid == 'bb51bb2b-1e14-4915-8114-58085b952c8f')
    # user = Users.get(Users.username == 'tima1')
    # print(user.email)
    # print(update_exchange_status_ticket(ticket_number='ebb94499-05c9-494f-9f4a-402c6543f244',
    #                                     user=Users.get(Users.username == 'tima1')))
    # print(exchange_ticket(user=Users.get(Users.username == 'tima1')))
    # create_ticket()
    print(exchange_ticket(username='tima', user_uuid='576e779d-be7a-4632-bbdc-d6812bcb48d4'))
