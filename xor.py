action = input("1. Encryption\n2. Decryption\nChoose(1,2): ")

def encrypt():
    text = input("Enter string: ")
    key = input("Enter key: ")

    encrypt_hex = ""
    key_itr = 0
    for i in range(len(text)):
        temp = ord(text[i]) ^ ord(key[key_itr])
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Encrypted Text: " + format(encrypt_hex))

def decrypt():
    text = input("Enter string: ")
    key = input("Enter key: ")

    hex_to_uni = ""
    for i in range(0, len(text), 2):
        hex_to_uni += bytes.fromhex(text[i:i+2]).decode('utf-8')

    decryp_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Decrypted Text: " + format(decryp_text))

if action == '1':
    print("---Encryption---")
    encrypt()
elif action == '2':
    print("---Decryption---")
    decrypt()
else:
    print("Invalid Choice!")


