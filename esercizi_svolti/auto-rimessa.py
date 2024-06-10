class Veicolo:
    def __init__(self, marca: str, alimentazione: str):
        self.__marca = marca
        self.__alimentazione = alimentazione

    def get_marca(self):
        return self.__marca
    
    def get_alimentazione(self):
        return self.__alimentazione

    def set_marca(self, nuova_marca):
        self.__marca= nuova_marca

    def set_alimentazione(self, nuova_alimentazione):
        self.__alimentazione= nuova_alimentazione

    def __str__(self):
        return f"Marca: {self.__marca}, Alimentazione: {self.__alimentazione}"

#veicolo1= Veicolo("Fiat", "Benzina")
#print (veicolo1.__str__())

class Furgone(Veicolo):
    def __init__(self, marca: str, alimentazione: str, capacita_massima: int):
        super().__init__(marca, alimentazione)
        self.__capacita_massima = capacita_massima

    def get_capacita_massima():
        return self.__capacita_massima
    
    def __str__(self):
        return f"{super().__str__()}, Capacità massima: {self.__capacita_massima}"

#veicolo2= Furgone("fiat", "Benzina", 10)
#print (veicolo2.__str__())

class Macchina(Veicolo):
    def __init__(self, marca: str, alimentazione: str, numero_porte: int):
        super().__init__(marca, alimentazione)
        self.__numero_porte = numero_porte

    def get_numero_porte(self):
        return self.__numero_porte
    
    def __str__(self):
        return f"{super().__str__()}, Numero di porte: {self.__numero_porte}"
    

class Autorimessa:
    def __init__(self , capienza_max):
        self.__capienza_max = capienza_max
        self.__veicoli = []

    def add_veicolo(veicolo : Veicolo):
        # ESISTE POSTO ??
        if  self.__capienza_max < len(self.__veicoli) +1:
            print("non esiste parcheggio")
            return -1

        for index in range(len( len(self.__veicoli))):
            if self.__veicoli[index] == None:  # posto vuoto
                self.__veicoli[index] = veicolo # parking
                return index # ritorno dove ho parcheggiato
        
        return -1


    def remove(pos) -> Veicolo:
        return self.__veicoli.pop(pos)



