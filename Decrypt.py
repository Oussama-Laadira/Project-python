import string
latter = string.ascii_letters
word = input("Enter a message The encoder: ")
number = int(input("Enter a shift number: "))
def Decrypt():
    Decrypt_message = ""
    for i in word :
        if i.lower() in latter:
            original_position = latter.index(i.lower())
            now_position = original_position - number
            Decrypt_latter = latter[now_position]
            if i.isupper():
                Decrypt_latter = Decrypt_latter.upper()
            Decrypt_message += Decrypt_latter
        else:
            Decrypt_message += i
    print(Decrypt_message)
Decrypt()
