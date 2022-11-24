from data_classes import *

# TODO Task 1 and 2

automobile1 = Auto('BMW', 4, 'red', 'G 10', 1800, 'Tima')
automobile2 = Auto('Mercedes', 3, 'blue', 's63', 2000, 'Tima')
truck1 = Truck('Jeep', 10, 'Black', 'Cheerokee', 2500, 'Tima', 3200)
truck2 = Truck('Toyota', 20, 'Gray', 'Land Cruiser 105', 2600, 'Viktor', 3500)
car1 = Car('Jaguar', 3, 'Black', 'XJ40', 1950, 'Tima', 320)
car2 = Car('KIA', 6, 'Pink', 'RIO', 1700, 'Oleg', 240)


def check_move_stop():
    print('''Движение  и остановка
___________________________''')
    automobile1.move()
    automobile2.move()
    truck1.move()
    truck2.move()
    car1.move()
    car2.move()
    automobile1.stop()
    automobile2.stop()
    truck1.stop()
    truck2.stop()
    car1.stop()
    car2.stop()


def check_load():
    print('''Погрузка
___________________________''')
    truck1.load()
    truck2.load()


def print_obj(*args):
    for i in args:
        i.get_info()  # or print


def make_old(years: int):
    print('''Старение
___________________________''')
    for i in range(years):
        automobile1.birthday()
        automobile2.birthday()
        truck1.birthday()
        truck2.birthday()
        car1.birthday()
        car2.birthday()


if __name__ == "__main__":
    check_move_stop()
    # check_load()
    print_obj(automobile1, automobile2, car2, car1, truck2, truck1)
    make_old(1)
