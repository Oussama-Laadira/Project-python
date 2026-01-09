import string
latter = string.ascii_letters
word = input("Enter a message The encoder: ")
number = int(input("Enter a shift number: "))
def hashe():
    encryptide = ""
    for i in word:
        if i.upper() in latter:
            original_position = latter.index(i)
            now_position = (original_position + number)
            crypt = latter[now_position]
            if i.isupper():
                crypt = crypt.upper()
            encryptide += crypt
        else:
            encryptide += i
    print(f"Encryption succeede:   {encryptide}")
hashe()