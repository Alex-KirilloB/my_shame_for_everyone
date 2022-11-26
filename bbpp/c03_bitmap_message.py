"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, artistic"""

import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print('Bitmap message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')

message = input('> ')
if message == '':
    sys.exit()

# Проходим в цикле по всем строкам битовой карты
for line in bitmap.splitlines():
    # Проходим по всем символам строки
    for i, bit in enumerate(line):
        if bit == ' ':
            # Выводим пробел в битовой карте
            print(bit, end='')
        else:
            # Выводим сивмол польз. сообщения
            print(message[i % len(message)], end='')
    print()  # Переходим на слею строку
