import base64

def main():
    action = input("1. Encryption\n2. Decryption\nChoose (1,2): ")

    def encrypt(text):
        string_bytes = text.encode("ascii")
        encode_bytes = base64.b64encode(string_bytes)
        result = encode_bytes.decode("ascii")
        return result

    def decrypt(text):
        string_bytes = text.encode("ascii")
        decode_bytes = base64.b64decode(string_bytes)
        result = decode_bytes.decode("ascii")
        return result

    if action == '1':
        print("---Encryption---")
        text = input("[+] Enter text: ")
        ciphertext = encrypt(text)
        print(f"[+] Cipher text: {ciphertext}")
    elif action == '2':
        print("---Decryption---")
        text = input("[+] Enter text: ")
        plaintext = decrypt(text)
        print(f"[+] Plain text: {plaintext}")
    else :
        print("Wrong Choice!")

if __name__ == '__main__':
    main()