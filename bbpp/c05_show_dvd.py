"""
Отскакивающий от краев логотип DVD
Анимация отскакивающего логотипа DVD. Оценишь, если достаточно стар
"""

import sys
import random
import time

try:
    import bext

except ImportError:
    print('this program requires the bext module, which you')
    print('can install by following instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# задаем константы
WIDTH, HEIGHT = bext.size()
# WIDTH, HEIGHT = 10, 5

# В Windows нельзя вывести символ в последний столбец без добавления
# автоматически символа новой строки, т.ч. уменьшаем ширину на 1
WIDTH -= 1
NUMBER_OF_LOGOS = 3
PAUSE_AMOUNT = 0.15
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Названия ключей для ассоциативных массивов логотипов
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()
    # print('\n', WIDTH, HEIGHT, '\n')

    # Генерация логотипов
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append(
            {
                COLOR: random.choice(COLORS),
                X: random.randint(1, WIDTH - 4),
                Y: random.randint(1, HEIGHT - 4),
                DIR: random.choice(DIRECTIONS)
                # DIR: DOWN_RIGHT
            }
        )
        if logos[-1][X] % 2 == 1:
            # Гарантируем, что X четное число, для столкновения с углом
            logos[-1][X] -= 1

        # print(logos[-1][X], logos[-1][Y])

    corner_bounces = 0  # Считаем, сколько раз логотип столкнулся с углом
    while True:  # основной цикл программы
        for logo in logos:  # Обрабатываем все логотипы в списке логотипов
            # Очищаем место, где ранее находился логотип
            bext.goto(logo[X], logo[Y])
            # print(logo[X], logo[Y], logo[DIR])
            print('   ', end='')

            original_direction = logo[DIR]

            # Проверка на отскакивание логотипа от угла
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                corner_bounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                corner_bounces += 1

            # Проверка, не отскакивает ли логотип от левого края
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # Проверка, не отскакивает ли логотип от правого края
            elif logo[X] == WIDTH - 2 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 2 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # Проверка, не отскакивает ли логотип от верхнего края
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # Проверка, не отскакивает ли логотип от нижнего края
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != original_direction:
                # Меняем цвет при отскакивании логотипа
                logo[COLOR] = random.choice(COLORS)

            # Перемещаем логотип (Координата X меняется на 2, поскольку
            # в терминале высота символов вдвое превышает ширину)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Отображает количество отскакиваний от углов
        bext.goto(5, 0)
        bext.fg('white')
        print('Courner bounces:', corner_bounces, end='')

        for logo in logos:
            # отрисовывает логотипы на новом месте
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()  # Необходимо для программ, использующих bext
        time.sleep(PAUSE_AMOUNT)


# Если программа не импортируется, а запускается, то запускаем
if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()  # при нажатии Ctrl+C завершаем выполнение программы
