text = input('Enter string: ')
translated = ''
i = len(text) - 1

while i >= 0:
   translated = translated + text[i]
   i = i - 1
print("Encrypted string: ",translated)