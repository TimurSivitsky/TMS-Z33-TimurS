from pprint import pprint

from data import temp
from functools import reduce





# TODO Определить какая максимальная температура была зафиксирована в течение месяца.
# TODO Task 1

def task_1(user_case: str = None):
    print(max(list(map(max, temp))))
    print(max([max(i) for i in temp]))
    print(max(reduce(lambda x, y: x if max(x) > max(y) else y, temp)))


# TODO Определить какая минимальная температура была зафиксирована в течение месяца.
# TODO Task 2

def task_2(user_case: str = None):
    print(min(list(map(min, temp))))
    print(min([min(i) for i in temp]))
    print(min(reduce(lambda x, y: x if min(x) < min(y) else y, temp)))


# TODO Вычислить среднюю температуру по дням и записать в новый словарь, где ключом будет номер дня, а значением средняя температура.
# TODO Task 3

def task_3(user_case: str = None) -> None:
    match user_case:
        case '1':
            avg: float
            avg_by_day: dict = {}
            for i, value in enumerate(temp):
                avg = (sum(value) / len(value)).__round__(2)
                avg_by_day[i + 1] = avg
            pprint(avg_by_day)

        case '2':
            print({day + 1: (sum(values) / len(values)).__round__(2) for day, values in enumerate(temp)})

        case '3':
            print(dict([day + 1, (sum(values) / len(values)).__round__(2)] for day, values in enumerate(temp)))


# TODO Отфильтровать данные так, чтобы оставить только те температуры, которые выше средней в этот день.
# TODO Task 4

def task_4(user_case: str = None) -> None:
    # result = (filter(lambda x: x > (sum(day_data) / len(day_data)).__round__(2), day_data) for day_data in temp)
    # print([list(x) for x in result])

    print([list(x) for x in
           (filter(lambda x: x > (sum(day_data) / len(day_data)).__round__(2), day_data) for day_data in temp)])


# TODO Создать новый список: процент зафиксированных температур, которые выше средней температуры в этот день.
# TODO Task 5

def task_5(user_case: str = None) -> None:
            print(*[list(ax) for ax in (
                map((lambda b: f'{len(b) * 100 / len(day_data)}%'),
                                            [list(x) for x in
                                             (filter(
                                                 lambda x: x > (sum(day_data) / len(day_data)).__round__(2), day_data)
                                                 for day_data in temp)]
                                            ) for day_data in temp)])


# TODO Определить какая максимальная температура была зафиксирована в течение месяца и указать в какой день.
# TODO Task 6

def task_6(user_case: str = None) -> None:

    print(*(list(map((lambda data: f'{max(data)} - {data.index(max(data))} день'), [list(dict([day + 1, (max(values)).__round__(2)] for day, values in enumerate(temp)).values())]))))


# TODO Определить какая минимальная температура была зафиксирована в течение месяца и указать в какой день.
# TODO Task 7

def task_7(user_case: str = None) -> None:
    print(*(list(map((lambda data: f'{min(data)} - {data.index(min(data))} день'),
                     [list(dict([day + 1, (min(values)).__round__(2)] for day, values in enumerate(temp)).values())]))))


def choose_task(func:str):
    print(f'{func} has been chosen')
    eval(func)()


if __name__ == "__main__":
    try:
        choose_task(input(f'Choose task which you wanna run \n {["task_7","task_6", "task_3", "task_5", "task_4", "task_1", "task_2"]} \n Input the func name: \t'))
    except Exception as e:
        print('Incorrect name', e)
