class StateNieMaMonety:
    
    def __init__(self, automat) -> None:
        self.automat = automat
        
    def włoż_monetę(self) -> None:
        print("Moneta przyjęta")
        self.automat.ustaw_stan(self.automat.pobierz_stan_jest_moneta())

    def zwróć_monetę(self) -> None:
        print("Nie włożyłeś monety")

    def przekręć_gałkę(self) -> None:
        print("Zanim przekręcisz gałkę, wrzuć monetę")

    def wydaj(self) -> None:
        print("Najpierw zapłać!")