from animals import PackAnimals


class Donkey(PackAnimals):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.specie = 'Осел'

    def pick_up_cargo(self):
        print('Берет груз')


class Horse(PackAnimals):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.specie = 'Лошадь'

    def pick_up_cargo(self):
        print('верховая езда')


class Mule(PackAnimals):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.specie = 'Мул'

    def pick_up_cargo(self):
        print('Берет груз')
