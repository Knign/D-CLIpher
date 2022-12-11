import base64

action = input("1. Encryption\n2. Decryption\nChoose (1,2): ")

def encrypt():
    string = input('Enter the string: ')
    string_bytes = string.encode("ascii")
    encode_bytes = base64.b64encode(string_bytes)
    encode_string = encode_bytes.decode("ascii")
    print("Encrypted string: " + encode_string)

def decrypt():
    string = input('Enter the string: ')
    string_bytes = string.encode("ascii")
    decode_bytes = base64.b64decode(string_bytes)
    decode_string = decode_bytes.decode("ascii")
    print("Decrypted string: " + decode_string)

if action == '1':
    print("---Encryption---")
    encrypt();
elif action == '2':
    print("---Decryption---")
    decrypt();
else :
    print("Wrong Choice!")
