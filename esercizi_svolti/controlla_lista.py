import random


def controlla_tutti_pari(my_lista):
    for elemento in (my_lista):
        if elemento % 2 != 0 :
            return False
        
    return True


def controlla_pari_v2(my_lista):
    sono_tutti_pari = True

    for elemento in (my_lista):
        if elemento % 2 != 0 :
            sono_tutti_pari = False
            break
    
    return sono_tutti_pari




def trova_massimo(my_lista):
    max=my_lista[ 0 ]

    for elemento in my_lista :
        if elemento > max :
            max = elemento
        # fine for

    return max


print(trova_massimo([1 , 77 , 66 , 13 ,3]))




def scegli_esercizio():
    lista_canditati = ["bash" , "python" , "reti" , "nulla"]
    return random.choice(lista_canditati)

print("#########################")
print(scegli_esercizio())
print("#########################")

