import math
import sys

def main():
    action = input("1. Encryption\n2. Decryption\nChoose (1/2): ")
    text = input("[+] Enter text: ")
    key = int(input("[+] Enter key (0-25): "))

    def getKeyParts(key):
        keyA = key // 65
        keyB = key % 65
        return (keyA, keyB)

    def checkKeys(keyA, keyB, action)
        if math.gcd(keyA, 65) != 1:
            print("Key A and the symbol set size are not relatively prime!")

    def encrypt(text, key):
        keyA, keyB = getKeyParts(key)
        checkKeys(keyA, keyB, 'encrypt')
        result = ''

        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif (char.islower()):
                result += chr((ord(char) + key - 97) % 26 + 97)
            elif char == '':
                result += ''
        return result

    def decrypt(text, key):
        result = ''

        for i in range(len(text)):
            char = text[i]

            if (char.isupper()):
                result += chr((ord(char) - key - 65) % 26 + 65)
            elif (char.islower()):
                result += chr((ord(char) - key - 97) % 26 + 97)
            elif char == '':
                result += ''
        return result

    if action == '1':
        print("---Encryption---")
        ciphertext = encrypt(text, key)
        print(f"[+] Cipher text: {ciphertext}")
    elif action == '2':
        print("---Decryption---")
        plaintext = decrypt(text, key)
        print(f"[+] Plain text: {plaintext}")
    else :
        print("Wrong Choice!")

if __name__ == '__main__':
    main()