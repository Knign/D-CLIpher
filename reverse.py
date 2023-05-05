def main():
   text = input("[+] Enter text: ")
   result = ''
   i = len(text) - 1
   while i >= 0:
      result = result + text[i]
      i = i - 1
   print(f"[+] Cipher text: {result}")

if __name__ == '__main__':
   main()
