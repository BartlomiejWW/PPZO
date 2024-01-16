import random

class KontoBankowe:
    def __init__(self, numer_konta, posiadacz_konta, saldo=0):
        self.__numer_konta = numer_konta
        self.__posiadacz_konta = posiadacz_konta
        self.__saldo = saldo
        self.__transakcje = []

    def wplata(self, kwota):
        if kwota > 0:
            self.__saldo += kwota
            self.__transakcje.append(f"Wpłata {kwota} zł")
            print(f"Wpłata {kwota} zł udana. Nowe saldo: {self.__saldo} zł")
        else:
            print("Nieprawidłowa kwota wpłaty.")

    def wyplata(self, kwota):
        if kwota > 0 and kwota <= self.__saldo:
            self.__saldo -= kwota
            self.__transakcje.append(f"Wypłata {kwota} zł")
            print(f"Wypłata {kwota} zł udana. Nowe saldo: {self.__saldo} zł")
        elif kwota <= 0:
            print("Nieprawidłowa kwota wypłaty.")
        else:
            print("Niewystarczające środki.")

    def wyswietl_info(self):
        print(f"Numer konta: {self.__numer_konta}")
        print(f"Posiadacz konta: {self.__posiadacz_konta}")
        print(f"Saldo: {self.__saldo} zł")
        print("Historia transakcji:")
        for transakcja in self.__transakcje:
            print(f"- {transakcja}")

    @staticmethod
    def generuj_numer_konta():
        return ''.join(random.choice('0123456789') for _ in range(9))

# Przykładowe użycie klasy KontoBankowe
numer_konta = KontoBankowe.generuj_numer_konta()
konto1 = KontoBankowe(numer_konta=numer_konta, posiadacz_konta="Jan Kowalski", saldo=1000)

konto1.wplata(500)
konto1.wyplata(200)
konto1.wyswietl_info()
