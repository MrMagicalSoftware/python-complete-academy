import hashlib


def cifra_md5(word):
    ris = hashlib.md5(word.encode())
    return ris.hexdigest()

is_running = True

while is_running:
    user_input = input("press y to encrypt ")
    if(user_input == "y"):
        print("insert a word")
        print(cifra_md5(   input()   ))
    else:
        print("bye bye")
        is_running=False
   