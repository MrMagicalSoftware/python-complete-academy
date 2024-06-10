import random

def genera_numero():
    return random.randint(1 ,6)


def playing():
    numero_1 = genera_numero()
    numero_2 = genera_numero()
    print(f"valori {numero_1}  {numero_2}")
    if(numero_1 + numero_2 == 7):
        print("hai vinto")
    else:
        print("hai perso")
    

is_playing = True

while is_playing  :

    print("Vuoi giocare ai dadi ? y/N")
    risposta_utente = input()

    if(risposta_utente == "y"):
        print("ok iniziamo a giocare ... ..")
        playing()
    else:
        print("ciao ciao ")
        is_playing = False