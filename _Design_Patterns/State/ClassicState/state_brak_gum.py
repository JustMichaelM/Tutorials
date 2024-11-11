class StateBrakGum:    
    
    def __init__(self, automat) -> None:
        self.automat = automat
    
    def włoż_monetę(self) -> None:
        print("Nie można wrzucić moenty, automat jest pusty.")

    def zwróć_monetę(self) -> None:
        print("Nie można zwrócić monety, żadna moneta nie została wrzucona.")

    def przekręć_gałkę(self) -> None:
        print("Obróciłeś gałkę, ale automat jest pusty!")

    def wydaj(self) -> None:
        print("Nie wydano gumy")