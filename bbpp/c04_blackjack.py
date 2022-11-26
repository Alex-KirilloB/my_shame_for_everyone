"""
Блэк-джэк (с) Эл Свейгарт al@inventwithpython.com
Классическая карточная игра "двадцать одно"
"""

import random
import sys

# Константы
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.''')

    money = 5000
    while True:  # Основной цикл игры
        # Проверка на наличие у игрока деняк
        if money <= 0:
            print("You are broke!")
            print("Good thinking you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # Даем возможность игроку сделать ставку на раунд
        print('Money:', money)
        bet = get_bet(money)

        # Сдаем дилеру и игроку по две карты
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Обработка действий игрока
        print('Bet:', bet)
        while True:
            # Выполняем до тех пор, пока игрок
            # не скажет "хватит" или у него не будет перебор
            display_hands(player_hand, dealer_hand, False)
            print()

            # проверка на перебор игрока
            if get_hand_value(player_hand) > 21:
                break

            # Получаем ход игрок: H, S или D
            move = get_move(player_hand, money - bet)

            # Обработка ответа игрока
            if move == 'D':
                # Игрок удваивает, он может увеличить ставку
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f'Bet increased to {bet}')
                print('Bet:', bet)

            if move in ('H', 'D'):
                # "Еще" или "удваиваю": игрок берет еще карту
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}')
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    # Перебор у игрока
                    continue

            if move in ('S', 'D'):
                # "Хватит" или "удваиваю": переход хода к след игроку
                break

        # Обр-ка действий дилера
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # Дилер берет карту
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break  # Перебор у дилера
                input('Press Enter to continue...')
                print('\n\n')

        # Отображение итоговых карт на руках
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        # проверка выигрыша, проигрыша или ничьи игроков
        if dealer_value > 21:
            print(f'Dealer busts! You win ${bet}!')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print(f'You won ${bet}')
            money += bet
        elif player_value == dealer_value:
            print("It's a tie, the bet is returned to you")

        input("Press Enter to continue...")
        print('\n\n')


def get_bet(max_bet):
    """Спрашиваем игрока, сколько он ставит на раунд"""
    while True:
        # Продолжаем спрашивать пока
        # не будет введено допустимое значение
        print(f'How much do you bet? (1-{max_bet}, or QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # Если игрок не ответил - спрашиваем снова

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet  # Игрок ввел допустимое значение ставки


def get_deck():
    """Возвращаем список кортежей (номинал, масть) для всех 52 карт"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Добавляем числовые карты
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Добавляем фигурные карты и тузы
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """Отображаем карты игрока и дилера. Скрываем карты дилера
    если show_dealer_hand = False"""
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        # Скрываем первую карту дилера
        display_cards([BACKSIDE] + dealer_hand[1:])

    # отображаем карты игрока
    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards):
    """Возращаем стоимость карт. Фигурные карты стоят по 10,
    тузы - 11 или 1 очко. Эта функция выбирает подходящую стоимость карты"""
    value = 0
    number_of_aces = 0

    # Добавляем стоиомсть карты - не туза:
    for card in cards:
        rank = card[0]  # Карта - кртеж из номинала и масти
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('J', 'Q', 'K'):  # Фигурные карты стоят 10 очков
            value += 10
        else:
            value += int(rank)  # Стоимость числовых карты - их номинал

    # Добавляем стоимость тузов
    value += number_of_aces  # Добавляем 1 для каждого туза
    for i in range(number_of_aces):
        # Если можно добавить еще 10 - добавляем
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    """Отображаем все карты из списка карт"""
    rows = ['', '', '', '', '']  # Отображаем в каждой строке текст

    for i, card in enumerate(cards):
        rows[0] = ' ___ '  # Вывод верхней строки карты
        if card == BACKSIDE:
            # Вывод рубашки карты
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Вывод лицевой стороны карты
            rank, suit = card  # карта - кортеж из номинала и масти
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f"|_{rank.rjust(2, '_')}| "

    # Выводим все строки на экран
    for row in rows:
        print(row)


def get_move(player_hand, money):
    """Спрашиваем, какой ход хочет сделать игрок и возвращаем "H" если он
    хочет взять еще карту, "S", если ему хватит и "D", если он удваивает"""
    while True:
        # Продолжаем итерации пока игрок не сделает
        # допустимый ход

        # Определяем какие ходы может сделать игрок
        moves = ['(H)it', '(S)tand']

        # игрок может удвоить при первом ходе, это ясно из того,
        # что у игрока ровно две карты
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # получаем ход игрока
        move_promt = ', '.join(moves) + '> '
        move = input(move_promt).upper()
        if move in ('H', 'S'):
            return move  # Игрок сделал допустимый ход
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Игрок сделал допустимый ход


if __name__ == '__main__':
    main()
