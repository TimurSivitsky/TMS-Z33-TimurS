class Auto():

    def __init__(self, brand, age, color, mark, weight, owner):
        print(f'Экземпляр Auto класса \t{brand, age, color, mark, weight, owner} \t\t\t\t\t\t\tбыл создан ')

        self.__brand: str = brand
        self.__age: float = age
        self.__color: str = color
        self.__mark: str = mark
        self.__weight: float = weight
        self.owner: str = owner

    def get_info(self):
        return print(self)

    def move(self):
        print(f'Auto {self.__brand, self.__mark} поехала ')

    def birthday(self):
        self.__age += 1
        print(f'Постарел на год. Теперь мне {self.__age} ')

    def stop(self):
        print(f'Auto {self.__brand, self.__mark} остановилась ')

    def __str__(self):
        return f"""
        Brand: {self.__brand},
        Model: {self.__mark},
        Age: {self.__age} \t\ty.o.,
        Weight: {self.__weight} \tkg,
        Color: {self.__color},
        Owner: {self.owner}
        """


class Truck(Auto):

    def __init__(self, brand, age, color, mark, weight, owner, max_load):
        # super().__init__(brand, age, color, mark, weight, owner, max_load)
        super(Truck, self).__init__(brand, age, color, mark, weight, owner)

        # self.__brand: str = brand
        # self.__age: float = age
        # self.__color: str = color
        # self.__mark: str = mark
        # self.__weight: float = weight
        # self.owner: str = owner
        self.__max_load: float = max_load

        print(f'Экземпляр Truck класса \t{[brand, age, color, mark, weight, owner, max_load]} \t\t\t\tбыл создан')

        # return truck_init
    #
    def __str__(self):
        # super(Truck, self).__str__(self.__brand, self.age, self.color, self.mark, self.weight, self.owner)
        truck_str = super(Truck, self).__str__()

        return truck_str + f"""Max load: {self.__max_load} \tkg"""


    def move(self):
        print(f'Attention')
        super(Truck, self).move()
