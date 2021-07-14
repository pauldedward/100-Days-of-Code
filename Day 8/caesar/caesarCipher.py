
direction = input("Type 'e' for encryption or 'd' for decryption: ")

if direction != 'e' and direction != 'd':
    print("Error: Invalid direction")
    exit()

message = input("Enter the message: ")
caesarNumber = int(input("Enter the number of shifts: "))


def cipherUnrestricted(message, direction, caesarNumber):
    cipheredMessage = ""
    if direction == 'e':
        for letter in message:
            if letter.isalpha():
                cipheredMessage += chr((ord(letter) -
                                        97 + caesarNumber) % 26 + 97)
            else:
                cipheredMessage += chr((ord(letter) -
                                        48 + caesarNumber) % 10 + 48)
        return cipheredMessage
    elif direction == 'd':
        for letter in message:
            if letter.isalpha():
                cipheredMessage += chr((ord(letter) -
                                        97 - caesarNumber) % 26 + 97)
            else:
                cipheredMessage += chr((ord(letter) -
                                        48 - caesarNumber) % 10 + 48)
        return cipheredMessage


print(cipherUnrestricted(message, direction, caesarNumber))
