"""
Взлом шифра Цезаря
Взлом сообщений, зашифрованных шифром Цезаря
путем перебора всех возможных ключей
"""

print('Caesar cipher hacker')

# пользователь вводит сообщение
print('Enter the encrypted message to hack')
message = input('> ').upper()

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    # Расшифровка
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num -= key

            if num < 0:
                num += len(SYMBOLS)

            translated += SYMBOLS[num]

        else:
            translated += symbol

    # Вывод ключа вместе с расшифрованным текстом
    print(f'Key #{key}: {translated}')
