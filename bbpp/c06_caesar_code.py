"""
Шифр Цезаря
Шифрование и шешифрование происходит путем сдвига каждого символа алфавита
на определенное число мест
"""

try:
    import pyperclip
except ImportError:
    pass

# Алфавит
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Шифр или дешифр
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')

# Ввод ключа
while True:
    max_key = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {max_key}) to use.')
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Ввод сообщения для штфрования/дешифрования
print(f'Enter the message to {mode}.')
message = input('> ').upper()

# Answer
translated = ''

# Шифрование/дешифрование
for symbol in message:
    if symbol in SYMBOLS:
        # Числовое значение символа
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        # Добавление символа без шифрования
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard')
except:
    pass
