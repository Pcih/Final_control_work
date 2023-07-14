import re


def select_menu(menu: tuple | list, prompt: str = None, end=' | ') -> tuple[int, str]:
    if prompt is None:
        prompt = 'Выберите из меню'
    d = len(str(len(menu)))
    print('-' * 15)
    for index, name in enumerate(menu, 1):
        print(f'{index:>{d}}: {name}', end=end)
    print(f'{"0":>{d}}: Выход')
    print(f'\n{prompt}:')
    answer = input('> ')
    if answer.isdigit() and (index := int(answer) - 1) in range(len(menu)):
        return index, menu[index]
    if answer.lower() in map(lambda s: s.lower(), menu):
        find_index = list(map(lambda s: s.lower(), menu)).index(answer.lower())
        return find_index, menu[find_index]
    return -1, 'Выход'


def confirm_action(prompt=None) -> bool:
    if prompt is None:
        prompt = 'Подтвердите действие'
    prompt += ' (Да/нет): '
    answer = input(prompt)
    if answer in ('да', 'yes', 'д', 'y'):
        return True
    else:
        return False


def input_date(prompt) -> str:
    def validate_date(date_string):
        pattern = r'^\d{4}-\d{2}-\d{2}$'  # Шаблон для проверки формата YYYY-MM-DD

        if re.match(pattern, date_string) and int(date_string.split('-')[1]) in range(1, 13):
            return True
        else:
            return False

    while True:
        date = input(prompt)
        if validate_date(date):
            return date
        else:
            print('Неправильный формат даты. Попробуйте еще раз.')
    return date
