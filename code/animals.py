from datetime import datetime
from abc import ABC, abstractmethod
from random import choice


class Animal(ABC):
    """
    Родительский класс.
    """

    def __init__(self, name, date_of_birth):
        self.name = name
        self.birth_date: datetime = datetime.strptime(date_of_birth, '%Y-%m-%d') \
            if isinstance(date_of_birth, str) else date_of_birth
        self.commands = []
        self.specie = None

    def add_commands(self, commands):
        self.commands.extend(map(lambda s: s.strip(), commands))

    def act_command(self):
        if self.commands:
            print(choice(self.commands))


class Pets(Animal, ABC):
    """
    Домашние животные
    """

    @abstractmethod
    def act(self):
        """
        Взаимодействие домашнего животного с человеком.
        """
        pass


class PackAnimals(Animal, ABC):
    """
    Домашние животные
    """

    @abstractmethod
    def pick_up_cargo(self):
        """
        Вьючные животные умеют брать груз.
        """
        pass
