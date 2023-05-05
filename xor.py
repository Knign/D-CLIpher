def main():
    action = input("1. Encryption\n2. Decryption\nChoose(1,2): ")

    def encrypt(text, key):
        result = ""
        key_itr = 0
        for i in range(len(text)):
            temp = ord(text[i]) ^ ord(key[key_itr])
            result += hex(temp)[2:].zfill(2)
            key_itr += 1
            if key_itr >= len(key):
                key_itr = 0
        return format(result)

    def decrypt(text, key):
        hex_to_uni = ""
        for i in range(0, len(text), 2):
            hex_to_uni += bytes.fromhex(text[i:i+2]).decode('utf-8')
        result = ""
        key_itr = 0
        for i in range(len(hex_to_uni)):
            temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
            result += chr(temp)
            key_itr += 1
            if key_itr >= len(key):
                key_itr = 0
        return format(result)

    if action == '1':
        print("---Encryption---")
        text = input("[+] Enter text: ")
        key = input("[+] Enter key: ")
        ciphertext = encrypt(text, key)
        print(f"[+] Cipher text: {ciphertext}")
    elif action == '2':
        print("---Decryption---")
        text = input("[+] Enter text: ")
        key = input("[+] Enter key: ")
        plaintext = decrypt(text, key)
        print(f"[+] Plain text: {plaintext}")
    else :
        print("Wrong Choice!")

if __name__ == '__main__':
    main()