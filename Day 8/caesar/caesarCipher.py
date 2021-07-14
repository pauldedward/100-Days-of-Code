import os


def clear(): return os.system('cls')


should_continue = True


def cipherUnrestricted(message, direction, caesarNumber):
    cipheredMessage = ""
    if direction == 'e':
        for letter in message:
            if letter.isalpha():
                cipheredMessage += chr((ord(letter) -
                                        97 + caesarNumber) % 26 + 97)
            else:
                characterNumber = ord(letter) - 48
                if characterNumber < 0 or characterNumber > 9:
                    cipheredMessage += letter
                else:
                    cipheredMessage += chr((characterNumber +
                                            caesarNumber) % 10 + 48)
        return cipheredMessage
    elif direction == 'd':
        for letter in message:
            if letter.isalpha():
                cipheredMessage += chr((ord(letter) -
                                        97 - caesarNumber) % 26 + 97)
            else:
                characterNumber = ord(letter) - 48
                if characterNumber < 0 or characterNumber > 9:
                    cipheredMessage += letter
                else:
                    cipheredMessage += chr((characterNumber -
                                            caesarNumber) % 10 + 48)
        return cipheredMessage


while should_continue:
    direction = input("Type 'e' for encryption or 'd' for decryption: ")

    if direction != 'e' and direction != 'd':
        print("Error: Invalid direction")
        continue

    clear()
    mode = "Encryption mode" if direction == 'e' else "Decryption mode"
    print(mode)
    message = input("Enter the message: ")
    caesarNumber = int(input("Enter the number of shifts: "))

    print(cipherUnrestricted(message, direction, caesarNumber))

    should_continue = input("Continue? (y/n): ") == 'y'

