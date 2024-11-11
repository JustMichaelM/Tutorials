"""Raczej ludzie tworzą ten design pattern w ten sam klasyczny sposób. Bez żadnej kombinatoryki z enumami itp, itd."""

from typing import Protocol, Final

class StateInterface(Protocol):
        
        def make_action(self) -> None: ...

class DroidInterface(Protocol):
    
    def switch_state(self, new_state: 'StateInterface') -> None:...

    def make_action(self) -> None: ...

    def print(self) -> None: ...

class IdleState:
    
    def make_action(self) -> None:
        print("**Do nothing**")
    
    def __str__(self) -> str:
        return "Idle State"

class MoveState:
    
    def make_action(self) -> None:
        print("Move Move")

    def __str__(self) -> str:
        return "Move State"

class AttackState:
    
    def make_action(self) -> None:
        print("Roger Roger")

    def __str__(self) -> str:
        return "Attack State"

class B1BattleDroid:

    IDLE_STATE: Final[StateInterface] = IdleState()
    MOVE_STATE: Final[StateInterface] = MoveState()
    ATTACK_STATE: Final[StateInterface] = AttackState()

    def __init__(self) -> None:
        self.state: StateInterface = B1BattleDroid.IDLE_STATE

    def switch_state(self, new_state: 'StateInterface') -> None:
        if self.state != new_state:
            self.state = new_state
        else:
            print("Droid jest już w tym stanie")

    def make_action(self) -> None:
        self.state.make_action()

    def print(self) -> None:
        print(f"Droid jest w stanie: {self.state}")

def main():
    b1_droid = B1BattleDroid()
    b1_droid.print()

    b1_droid.switch_state(B1BattleDroid.MOVE_STATE)
    b1_droid.print()

    b1_droid.switch_state(B1BattleDroid.IDLE_STATE)
    b1_droid.print()

    b1_droid.switch_state(B1BattleDroid.ATTACK_STATE)
    b1_droid.print()

    b1_droid.switch_state(B1BattleDroid.ATTACK_STATE)

if __name__ == "__main__":
    main()


