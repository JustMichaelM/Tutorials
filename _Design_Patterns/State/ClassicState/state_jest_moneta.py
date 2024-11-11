from random import randint

class StateJestMoneta:

    def __init__(self, automat) -> None:
        self.automat = automat

    def włoż_monetę(self) -> None:
        print("Nie możesz włożyć więcej niż jednej monety")

    def zwróć_monetę(self) -> None:
        print("Moneta zwrócona")
        self.automat.ustaw_stan(self.automat.pobierz_stan_nie_ma_monety())

    def przekręć_gałkę(self) -> None:
        wygrana: int = randint(1,10)

        print("Obróciłeś gałkę")
        if wygrana == 10:
            self.automat.ustaw_stan(self.automat.pobierz_stan_wygrana())
        else:
            self.automat.ustaw_stan(self.automat.pobierz_stan_guma_sprzedana())

    def wydaj(self) -> None:
        print("Nie wydano gumy")