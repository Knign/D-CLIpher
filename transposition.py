import pyperclip
import math

action = input("1. Encryption\n2. Decryption\nChoose (1,2): ")

def encrypt():
    text = input('Enter string: ')
    key = int(input('Enter key length: '))

    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(text):
            ciphertext[col] += text[position]
            position += key
    return ''.join(ciphertext)

def decrypt():
    text = input('Enter string: ')
    key = int(input('Enter key length: '))

    numOfColumns = math.ceil(len(text) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)
    plaintext = float('') * numOfColumns
    col = 0
    row = 0

    for symbol in text:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

if action == '1':
    print("---Encryption---")
    ciphertext = encrypt()
    print("Encrypted string: " + ciphertext)
    pyperclip.copy(ciphertext)
elif action == '2':
    print("---Decryption---")
    plaintext = decrypt()
    print("Decrypted string: "+ plaintext)
else:
    print("Wrong Choice!")