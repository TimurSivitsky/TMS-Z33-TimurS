import jwt
from ne_magazin.models import Users


def parse_username_and_points(token):
    decoded_dict = jwt.decode(jwt=token, key="tima_secret", algorithms='HS256')
    username = decoded_dict['username']
    user_id = decoded_dict['uuid']
    # points: Users = Users.get(Users.username == username)
    # points: int = int(points.points)

    return {"username": username, "user_id": user_id}


def get_data_from_user_dict(data: dict):
    return data['username'], data['user_id']


if __name__ == "__main__":
    print(parse_username_and_points(
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODY4Y2QyMmEtZjQ0Zi00NTEwLWJiN2MtN2FhZWQwN2RkMGRjIiwidXNlcm5hbWUiOiJpaGFyIiwiZW1haWwiOiJpaGFyIiwibGFzdF9sb2dpbiI6IjIwMjItMTItMTIgMjI6NDM6MzcuNjU0NDAyIn0.iVNDgOtmzdF4SJTx5u9oyZtbIjf85yf2CZyaVUq2FKE'))
