from typing import Final

from state_interface import State
from state_brak_gum import StateBrakGum
from state_nie_ma_monety import StateNieMaMonety
from state_guma_sprzedana import StateGumaSprzedana
from state_jest_moneta import StateJestMoneta 
from state_wygrana import StateWygrana

from random import randint

class Automat:

    def __init__(self, liczba_gum: int) -> None:
        self.BRAK_GUM: Final['StateBrakGum'] = StateBrakGum(self)
        self.NIE_MA_MONETY: Final['StateNieMaMonety'] = StateNieMaMonety(self)
        self.JEST_MONETA: Final['StateJestMoneta'] = StateJestMoneta(self)
        self.GUMA_SPRZEDANA: Final['StateGumaSprzedana'] = StateGumaSprzedana(self)
        self.WYGRANA: Final['StateWygrana'] = StateWygrana(self)

        self.stan: 'State' = self.BRAK_GUM 
        self.liczba_gum: int = liczba_gum
        
        if self.liczba_gum > 0:
            self.stan = self.NIE_MA_MONETY

    def włóż_monetę(self) -> None:
        self.stan.włoż_monetę()

    def zwróć_monetę(self) -> None:
        self.stan.zwróć_monetę()

    def przekręć_gałkę(self) -> None:
        self.stan.przekręć_gałkę()
        self.stan.wydaj()

    def ustaw_stan(self, stan: 'State') -> None:
        self.stan = stan
        
    def zwolnij_gumę(self) -> None:
        print("Wypada guma...")
        if self.liczba_gum != 0:
            self.liczba_gum -= 1

    def pobierz_stan_brak_gum(self) -> 'State':
        return self.BRAK_GUM
    
    def pobierz_stan_nie_ma_monety(self) -> 'State':
        return self.NIE_MA_MONETY
    
    def pobierz_stan_jest_moneta(self) -> 'State':
        return self.JEST_MONETA
    
    def pobierz_stan_guma_sprzedana(self) -> 'State':
        return self.GUMA_SPRZEDANA
    
    def pobierz_stan_wygrana(self) -> 'State':
        return self.WYGRANA

    def pobierz_liczbę_gum(self) -> int:
        return self.liczba_gum

    def __str__(self) -> str:
        return f"Witamy w Automacie do gum!\nStan automatu: {self.stan}\nLiczba gum w automacie: {self.liczba_gum}"


