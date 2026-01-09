import random
import string
def code_1():
    code = int(input("welcome to the Password Generator! \n Enter rhe total nimber of characters in the password: "))
    number_Letters = int(input("Enter the number of letters in the password: "))

    number_Number = int(input("Enter the number of number in the password: "))

    number_Symbols = int(input("Enter the number of symbols in the password: "))

    if code == number_Symbols+number_Number+number_Letters :
        a = random.choices(string.ascii_letters, k=number_Letters)
        b = random.choices(string.digits, k=number_Number)
        c = random.choices(string.punctuation, k=number_Symbols)
        final = (a + b + c)
        final_Key = "".join(final)
        print("Generated Password: " + final_Key)


    else:
        print("ples agen")
code_1()
def chewa_2() :
    code_2 = input("Do you want to reset my password or change? <yes or no>: ").lower()
    if code_2 == "yes" :
        code_1()
        print("😉😊")
    elif code_2 == "no" :
        print("ok by ☺")
    else:
        print("check your entered incoreectly ... ")
        chewa_2()
chewa_2()