from data_classes import *


# TODO Task 1

def test_car():
    print(new_car)
    new_car.move()
    new_car.move()
    new_car.stop()
    new_car.move()
    new_car.stop()

    new_car.birthday()
    new_car.birthday()
    new_car.birthday()
    new_car.birthday()

    new_car.owner

    new_car.get_info()


# print(new_car)


# TODO TASK 2
# truck = Truck('Jeep', 10, 'Black', 'Cheerokee', 2500, 'Tima', 3500)

if __name__ == "__main__":
    new_car = Auto('BMW', 10, 'red', 'G 10', 2000, 'Tima')
    # truck = Truck('Jeep', 10, 'Black', 'Cheerokee', 2500, 'Tima', 3500)
    truck = Truck('Jeep', 10, 'Black', 'Cheerokee', 2500, 'Tima', 3500)

    # truck.max_load = 2500
    #
    # truck.get_info()
    # print(truck.max_load)
    # print(truck)
    # print(new_car)

    truck.move()
    print(truck)