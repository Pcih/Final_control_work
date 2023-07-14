import db_io
from animals_list import AnimalList
import user_interface as ui
from configs import animal_species
from configs import main_menu
from configs import animal_menu


def add_new_animal():
    name = input('Имя: ')
    date_of_birth = ui.input_date('Дата рождения (ГГГ-ММ-ДД): ')
    index, specie = ui.select_menu(tuple(map(lambda a: a[0], animal_species)), 'Выберите вид')
    if index != -1:
        animals.add_new_animal(name, date_of_birth, animal_species[index][1])


def add_new_command(animal_id):
    new_commands = input('Обучить команде (или нескольким через запятую): ').split(',')
    animals.add_command(animal_id, new_commands)


def delete_animal(animal_id):
    name = animals.get_animal(animal_id).name
    if ui.confirm_action(f'Точно удалить запись {name}?'):
        animals.delete_animal(animal_id)
        print(f'Запись {name} удалена')


def get_more_info(animal_id):
    print(animals.get_animal_info(animal_id))
    index, select = ui.select_menu(animal_menu)
    match index:
        case 0:
            add_new_command(animal_id)
        case 1:
            delete_animal(animal_id)


def main_polling():
    select = ''
    while select != 'Выход':
        select_index, select = ui.select_menu(main_menu)
        match select_index:
            case 0:
                animal_index, _ = ui.select_menu(animals.get_animals_list(),
                                                 'Для подробностей введите № животного', '\n')
                if animal_index != -1:
                    get_more_info(animal_index)
            case 1:
                add_new_animal()
            case _:
                pass


if __name__ == '__main__':
    animals = AnimalList()
    main_polling()
