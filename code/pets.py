from animals import Pets


class Cat(Pets):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.specie = 'Кошка'

    def act(self):
        print('Мяу')


class Dog(Pets):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.specie = 'Собака'

    def act(self):
        print('Гав-гав')


class Hamster(Pets):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.specie = 'Хомяк'

    def act(self):
        print('Бежит в колесе')


class Cow(Pets):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.specie = 'Корова'

    def act(self):
        print('Муу-уу')
