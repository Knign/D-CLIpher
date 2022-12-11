action = input("1. Encryption\n2. Decryption\nChoose (1,2): ")

def encrypt():
    text = input('Enter string: ')
    key = int(input('Enter the key length: '))

    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):

        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    print("Encrypted text: " + result)


def decrypt():
    text = input('Enter string: ')
    key = int(input('Enter the key length: '))

    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(text)):
            if ((rail[i][j] == '*') and
                    (index < len(text))):
                rail[i][j] = text[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(text)):

        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return result


if action == '1':
    print("---Encryption---")
    encrypt()
elif action == '2':
    print("---Decryption---")
    decrypt()
else :
    print("Wrong Choice!")
