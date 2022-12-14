from ne_magazin.views.handlers.decoder_token import parse_username_and_points
from ne_magazin.settings import menu_items_map
from ne_magazin.settings import intro
from ne_magazin.views.tickets import exchange_ticket
from ne_magazin.views.products import products_list_view
from ne_magazin.views.orders import launch_order_view
from ne_magazin.views.profile import profile_view


@intro
def executer_and_render_second_menu(username, user_uuid):

    while True:
        # print(welcome_msg)
        print(
f"""Для взаимодействия выберете номер команды:

> 1 - {menu_items_map['after_login_view'][0]}
> 2 - {menu_items_map['after_login_view'][1]}
> 3 - {menu_items_map['after_login_view'][2]}
> 4 - {menu_items_map['after_login_view'][3]}
> 5 - {menu_items_map['after_login_view'][4]}""")

        input_choice = input("> ").replace(' ', '')

        match input_choice:
            case '1':
                print("Товары")
                exit_reslut = products_list_view()

            case '2':
                result_order = launch_order_view(username)
                if result_order == False:
                    return False
                elif bool(result_order) == True:
                    print(f"Заказ успешно оформлен! Номер заказа: {result_order.order_uuid}")
                    return False

            case '3':
                exit_reslut = profile_view(username)
            case '4':
                print('Ticket')
                result_ticket = exchange_ticket(username, user_uuid)
                if result_ticket == False:
                    return False
                elif result_ticket == True:
                    return False

                print('Ticket')
                return False


            case '5':

                #TODO LOGOUT
                return "Logout"


            case _:
                print(f'неправильный выбор: \'{input_choice}\'  Попробуйте еще раз\n')



def is_token(token=None):
    if token:
        user_data = parse_username_and_points(token)
        try:
            username = user_data['username']
            # points = user_data['points']
            user_uuid = user_data["uuid"]
            # render_second_view_menu(username, points, user_uuid)
            return True

        except Exception as e:
            print(f"parse dict from token! something went wrong: {e}")
            return False
            # raise Exception('Have no token', e)


    else:
        raise Exception('Have no token')



def launch_second_view(token):
    if token:
        user_data = parse_username_and_points(token)

        a = executer_and_render_second_menu(user_data['username'], user_data['user_id'])
        while a == False:
            a = executer_and_render_second_menu(user_data['username'], user_data['user_id'])

        if a == "Logout":
            return "Logout"

        pass





if __name__ == "__main__":
    # print(is_token('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODY4Y2QyMmEtZjQ0Zi00NTEwLWJiN2MtN2FhZWQwN2RkMGRjIiwidXNlcm5hbWUiOiJpaGFyIiwiZW1haWwiOiJpaGFyIiwibGFzdF9sb2dpbiI6IjIwMjItMTItMTIgMjI6NDM6MzcuNjU0NDAyIn0.iVNDgOtmzdF4SJTx5u9oyZtbIjf85yf2CZyaVUq2FKE'))
    # print(render_second_view_menu(None,None))
# def launch_second_view()
#     a = render_second_view_menu(username='tima', user_uuid='576e779d-be7a-4632-bbdc-d6812bcb48d4')
#     while a == False:
#         a = render_second_view_menu(username='tima', user_uuid='576e779d-be7a-4632-bbdc-d6812bcb48d4')
#     pass
    launch_second_view('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMTA1NjhjYjAtMjJjNy00ZmM4LThjZjYtYWZiZDU0YzUxNzhlIiwidXNlcm5hbWUiOiJkYXJhIiwiZW1haWwiOiJkYXJhIiwibGFzdF9sb2dpbiI6IjIwMjItMTItMTMgMTI6MzQ6MTUuMzYxMjM1In0.0ZGpW1HIjc13AvcN6S2vpGf6azSKhWxpZWhjqqH2ij8')