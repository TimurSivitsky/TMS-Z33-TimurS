import time


class Auto():

    def __init__(self, brand, age, color, mark, weight, owner):
        # print(f'Экземпляр Auto класса \t{brand, age, color, mark, weight, owner} \t\t\t\t\t\t\tбыл создан ')
        self.__brand: str = brand
        self.__age: float = age
        self.__color: str = color
        self.__mark: str = mark
        self.__weight: float = weight
        self.owner: str = owner

    def get_info(self):
        return print(self)

    def move(self):
        print(f'{self.__brand} {self.__mark} поехала ')

    def birthday(self):
        self.__age += 1
        print(f'{self.__class__.__name__}: {self.__brand} {self.__mark} Постарел на год. Теперь возраст {self.__age} лет ')

    def stop(self):
        print(f'{self.__class__.__name__}: {self.__brand} {self.__mark} остановилась ')

    def __str__(self):
        return f"""
        ______________________________________
        || Brand: {self.__brand},
        || Model: {self.__mark},
        || Age: {self.__age} \t\ty.o.,
        || Weight: {self.__weight} \tkg,
        || Color: {self.__color},
        || Owner: {self.owner}"""


class Truck(Auto):

    def __init__(self, brand, age, color, mark, weight, owner, max_load):
        # print(f'Экземпляр Truck класса \t{[brand, age, color, mark, weight, owner, max_load]} \t\t\t\tбыл создан')
        super().__init__(brand, age, color, mark, weight, owner)
        self.__max_load: float = max_load

    def __str__(self):
        truck_str = super().__str__()

        return truck_str + f"""
        || Max load: {self.__max_load} \tkg
        """

    def move(self):
        print(f'Attention')
        super(Truck, self).move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, owner, max_speed):
        super().__init__(brand, age, color, mark, weight, owner)
        self.__max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.__max_speed}')

    def __str__(self):
        car = super().__str__()

        return car + f"""
        || Max speed: {self.__max_speed} \tkmh
        """
