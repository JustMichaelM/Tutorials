class StateGumaSprzedana:
    
    def __init__(self, automat) -> None:
        self.automat = automat

    def włoż_monetę(self) -> None:
        print("Proszę czekać na gumę")

    def zwróć_monetę(self) -> None:
        print("Niestety nie można zwrócić moenty po przekręceniu gałki")

    def przekręć_gałkę(self) -> None:
        print("Nie dostaniesz gumy tylko dlatego że przekręciłeś drugi raz!")

    def wydaj(self) -> None:
        self.automat.zwolnij_gumę()
        if self.automat.pobierz_liczbę_gum() > 0:
            self.automat.ustaw_stan(self.automat.pobierz_stan_nie_ma_monety())
        else:
            print("Koniec gum!")
            self.automat.ustaw_stan(self.automat.pobierz_stan_brak_gum())