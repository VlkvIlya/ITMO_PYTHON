class Building:

    def __init__(self, square, price, people):
        self.square = square
        self.price = price
        self.people = people

    # 1 метод
    def final_price(self):
        return self.square * self.price

    # 2 метод
    def relation(self):
        if self.people == 0:
            return 0
        else:
            return building.final_price() / self.people

    def info(self):
        print(f'Площадь: {self.square} м^3')
        print(f"Цена за м^2: {self.price} руб")
        print(f'Кол-во людей: {self.people}')



class village_house(Building):

    def __init__(self, square, price, people, dvor):
    # dvor - новый аргумент, двор
        super().__init__(square, price, people)
        self.dvor = dvor

    # 1 метод
    def final_price(self):
        if self.dvor:
            return self.square * self.price * 1.1
        else:
            return self.square * self.price
        # при наличии двора дороже на 10 процентов

    # 2 метод
    def relation(self):
        if self.people == 0:
            return 0
        else:
            return village.final_price() / self.people

    def info(self):
        super().info()
        print(f'Наличие двора: {self.dvor}')
        print(f'Соотношение стоимости к числу проживающих: {village.relation()}')




class city_flat(Building):

    def __init__(self, square, price, people, numb_floor):
    # numb_floor - новый аргумент, номер этажа
        super().__init__(square, price, people)
        self.numb_floor = numb_floor

    # 1 метод
    def final_price(self):
        return self.square * self.price * float(f'1.{self.numb_floor}')
        # дороже на кол-во процентов, равное номеру этажа

    # 2 метод
    def relation(self):
        if self.people == 0:
            return 0
        else:
            return city.final_price() / self.people

    def info(self):
        super().info()
        print(f'Этаж: {self.numb_floor}')
        print(f'Соотношение стоимости к числу проживающих: {city.relation()}')


building = Building(100, 15, 2)
village = village_house(100, 15, 2, True)
city = city_flat(100, 15, 2, 30)

print("\t=== Рынок ===")
building.info()  # Убрал print() и f-string
print()
print("\t=== Деревня ===")
village.info()   # Убрал print() и f-string
print()
print("\t=== Город ===")
city.info()      # Убрал print() и f-string
print()