numero_utente = int ( input("inserisci un numero"))


if numero_utente % 3 == 0:
    print("numero pari")
    print(f"il resto vale {numero_utente % 2}")
else:
    print("numero dispari")
    print(f"il resto vale {numero_utente % 2}")


print("###################################")

nuovo_num = int ( input("inserisci un numero"))

if nuovo_num  % 3 == 0 :
    print(f"il numero {nuovo_num} è nella tabellina del 3")
else:
    print(f"il numero   {nuovo_num} NON è nella tabellina del 3")

print("###################################")




//Esercizio

numero_utente = int ( input("inserisci un numero"))


# commento singola linea


if numero_utente % 6 == 0 :
    print("ok")
else:
    print("no")


'''
if numero_utente % 2 == 0 and numero_utente % 3 == 0 :
    print("ok")
else:
    print("No")
'''

'''
if numero_utente % 2 == 0:
    if numero_utente % 3 == 0:
        print("ok")
    else:
        print("no")
else :
    print("No")   
''' 
