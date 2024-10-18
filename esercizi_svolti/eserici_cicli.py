
'''
# sercizi cicli python :


# creare un programma che prend e in ingrsso un numero
# il programma stampa tutti i numueri da 1 fino l numero insierito
# ES : 4  1 2 3 4.  
# ES : 5  1 2 3 4 5
# ES : 10 1 2 3. .. . ...10

numero_utente = int ( input("inserisci un numero"))

i = 1

while i <= numero_utente:
    print(i)
    i +=1
'''



'''
# creare un programma che stampa a video tutta la tabellina del 2 
#  2 * 0 = 0
#  2 * 1 = 2
# .........

i = 0
while i <= 10 :
    print(f"2 * {i} = {2 * i} ")
    i+=1

print("fine del programma")
'''


'''
# scrivere un programma che fa il conto alla rovescia 10 9 8 7 6 5 4 3 2 1
i = 10
while i >= 0:
    #print(i)
    
    if i > 0 :
        print(i)
    else:
        print("Auguri!")

    i-=1
'''


'''
# creare un programma che stampa tutti  i numeri compresi tra 20 e 30 ..

# 20 21 22 23 24 25 .. .. ..30


i = 20

while i <= 30:
    print(i)
    i+=1
    
'''


'''
# stampare a video tutti i numeri da 40 fino a 35

# 40 39 38 37 36 35


i = 40

while i >= 35 :
    print(i)
    i-=1
'''


# stampare a video tutti i numeri da 41 fino a 35 che sono pari

# 40 38 36 

i = 40
while i >= 35:
    
    if i % 2 != 0 :  # significa dire che è dispari
        print(i) 
    i-=2


