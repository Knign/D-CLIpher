action = input("1. Encryption\n2. Decryption\nChoose (1,2): ")

def encrypt():
    text = input('Enter string: ')
    shift = int(input('Enter the shift (0-25): '))
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char == ' ':
            result += ' '
    print("[+] Encrypted string: " + result)

def decrypt():
    text = input('Enter string: ')
    shift = int(input('Enter the shift (0-25): '))
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char == ' ':
            result += ' '
    print("[+] Decrypted string: " + result)

if action == '1':
    print("---Encryption---")
    encrypt()
elif action == '2':
    print("---Decryption---")
    decrypt()
else :
    print("Wrong Choice!")