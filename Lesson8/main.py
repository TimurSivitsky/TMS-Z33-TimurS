

# TODO Task 1



class Auto():

    def __init__(self, brand, age, color, mark, weight, owner):

        print(f'Экземпляр Auto класса {[brand, age, color, mark, weight]} ')

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



new_car = Auto('BMW', 10, 'red', 'G 10', 2000, 'Tima')
print(new_car)
new_car.move()
new_car.move()
new_car.move()
new_car.move()
new_car.move()
new_car.move()

new_car.birthday()
new_car.birthday()
new_car.birthday()
new_car.birthday()

new_car.owner

new_car.get_info()
# print(new_car)