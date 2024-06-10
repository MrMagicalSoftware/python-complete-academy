'''
Esecizio biblioteca python :


'''


class Libro:
    def __init__(self, titolo , autore , anno_pubblicazione  ):
        self.__disponibilita = True
        self.__titolo = titolo
        self.__autore = autore
        self.__anno_pubblicazione = anno_pubblicazione


    def set_disponibilita(self , disp):
        self.__disponibilita = disp

    def get_titolo(self):
        return self.__titolo

    def get_disponibilita(self) -> bool :
        return self.__disponibilita

    def get_autore(self):
        return self.__autore

    def get_anno_pubblicazione(self):
        return self.__anno_pubblicazione

    def __str__(self) -> str:
        return f"{self.__titolo} {self.__autore}  {self.__anno_pubblicazione} {self.__disponibilita}"




class Biblioteca:
    def __init__(self):
        self.__libri  = [] 

    def aggiungi_libro(self , libro : Libro):
        self.__libri.append(libro)

    def __str__(self) -> str:
        return "".join(str(element) + "\n" for element in  self.__libri)

    # rimuove un libro dalla biblioteca in base al titolo
    def rimuovi_libro(self , titolo):
        for book in self.__libri :
            if book.get_titolo() == titolo:
                self.__libri.remove(book)
                return 


    def cerca_libro(self , titolo):
        for book in self.__libri :
            if book.get_titolo() == titolo:
                return book
        return None

    ################## TO FIX IT ############################
    def cerca_libri_con_contains(self , title):
        ris = []
        for book in self.__libri :
            print(f"here --> {book}")
            if book.get_titolo() in title:
                print("i was here")
                ris.append(book)
        return ris


    ##prestito libro
    def prestito_libro(self , titolo):
        # 1 - devi verificare che esiste il titolo
        # 2 - se esiste il titolo devi verificare che il libro sia disponibile

        libro = self.cerca_libro(titolo) # richiamo la funzione della riga 55 cerca_libro

        if  libro and libro.get_disponibilita():
            print(f"ok prendi in prestito {libro.get_titolo()}")
            libro.set_disponibilita(False)
        else:
            print("libro non trovato oppure in prestito")


    ##restituisci libro

    def restituisci_libro(self, titolo):
        libro = self.cerca_libro(titolo)
        if libro and not libro.get_disponibilita():
            print("lIBRO RESTITUITO")
            libro.set_disponibilita(True)
        else:
            print("non trovato...")



    ##mostra libri disponibili

    def mostra_libri_disponibili(self):
        for book in self.__libri:
            if book.get_disponibilita() :
                print(book)
           



####################################################

book1 = Libro("The secrets 1" , "MR jones" , 2010)
book2 = Libro("The secrets 2" , "MR jones" , 2010)
book3= Libro("The secrets 3" , "MR jones" , 2010)
book4= Libro("The book" , "MR jones" , 2010)




biblioteca = Biblioteca()
biblioteca.aggiungi_libro(book1)
biblioteca.aggiungi_libro(book2)
biblioteca.aggiungi_libro(book3)
biblioteca.aggiungi_libro(book4)

print(biblioteca)

biblioteca.prestito_libro("The book")
biblioteca.prestito_libro("The book")

print("####################")
print(biblioteca)


biblioteca.restituisci_libro("The book")


print("####################")
print(biblioteca)



#print(biblioteca.cerca_libro("The secrets 2"))

#print(biblioteca.cerca_libri_con_contains("secrets"))

