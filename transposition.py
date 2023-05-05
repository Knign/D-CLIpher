import math

def main():
    action = input("1. Encryption\n2. Decryption\nChoose (1/2): ")

    def encrypt(text, key):
        result = [''] * key
        for column in range(key):
            currentindex = column
            while currentindex < len(text):
                result[column] += text[currentindex]
                currentindex += key
        return ''.join(result)

    def decrypt(text, key):
        numOfColumns = int(math.ceil(len(text) / key))
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)
        result = [''] * numOfColumns
        column = 0
        row = 0
        for symbol in text:
            result[column] += symbol
            column += 1
            if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                column = 0
                row += 1
        return ''.join(result)

    if action == '1':
        print("---Encryption---")
        text = input("[+] Enter text: ")
        key = int(input("[+] Enter key: "))
        ciphertext = encrypt(text, key)
        print(f"[+] Cipher text: {ciphertext}")
    elif action == '2':
        print("---Decryption---")
        text = input("[+] Enter text: ")
        key = int(input("[+] Enter key: "))
        plaintext = decrypt(text, key)
        print(f"[+] Plain text: {plaintext}")
    else:
        print("Wrong Choice!")

if __name__ == '__main__':
    main()