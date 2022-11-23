"""Имитационное моделирование парадокса дней рождения, (с) Эл Свейгарт
al@inventwithpython.com Изучаем неожиданные вероятности из "Парадокса
дней рождения". Больше информации в статье https://ru.wikipedia.org/wiki/Парадокс_дней_рождения
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: короткая, математическая, имитационное моделирование"""

import datetime
import random


def get_birthdays(number_of_birthdays):
    """Возвращаем список объектов дат для случайных дней рождения"""
    birthdays_list = []
    for n in range(number_of_birthdays):
        # Год в имитационном моделировании роли не играет, лишь
        # бы в объектах дней рождения он был одинаков.
        start_of_year = datetime.date(2001, 1, 1)

        # Получаем случайный день года
        random_numbers_of_days = datetime.timedelta(random.randint(0, 364))
        rand_birthday = start_of_year + random_numbers_of_days
        birthdays_list.append(rand_birthday)
    return birthdays_list


def get_match(birthdays_list):
    """Возвращаем объект даты дня рождения, встречающегося
    несколько раз в списке дней рождения"""
    if len(birthdays_list) == len(set(birthdays_list)):
        return None  # Все дни рождения различны, возвращаем None

    # Сравниваем все дни рождения друг с другом попарно
    for a, birthday_a in enumerate(birthdays_list):
        for b, birthday_b in enumerate(birthdays_list[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a  # Возвращаем найденное соответствие


# Отображаем вводную информацию
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Создаем кортеж названий месяцев по порядку
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Запрашиваем, пока пользователь не введет допустимое значение.
    print('How many birthdays shall I generate? (Min 2 and Max 100)')
    response = input('> ')
    if response.isdecimal and 1 < int(response) <= 100:
        num_bdays = int(response)
        break  # Пользователь ввел допустимое значение
print()

# Генерируем и отображаем дни рождения
print(f'Here are {num_bdays} birthdays:')
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Выводим запятую для каждого дня рождения после первого.
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')
print('\n')

# Выясняем, встречаются ли два совпадающих дня рождения.
match = get_match(birthdays)

# Отображаем результаты
print('In this simulation, ', end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print(f'multiple people have a birthday on {date_text}')
else:
    print('there are no matching birthdays')
print()

# Производим 100 000 операций имитационного моделирования
print(f'Generating {num_bdays} random birthdays 100,000 times...')
print('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
sim_match = 0  # Число операций моделирования с совпадающими днями рождения
for i in range(100_000):
    # Отображаем сообщение о выполнении каждые 10 000 операций
    if i % 10_000 == 0:
        print(f'{i} simulations run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) is not None:
        sim_match += 1
print('100,000 simulations run.')

# Отображаем результаты имитационного моделирования
probability = round(sim_match / 100_000 * 100, 2)
print(f'''Out of 100,000 simulations of {num_bdays} people, 
there was a matching birthday in that group {sim_match} times.
This means that {num_bdays} people have a {probability} % chance of
having a matching birthday in their group.
That\'s probably more than you would think!''')
