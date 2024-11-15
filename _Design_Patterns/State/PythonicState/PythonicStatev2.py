from enum import Enum, auto

class State(Enum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()

class Trigger(Enum):
    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


RULES = {
    State.OFF_HOOK: [
        (Trigger.CALL_DIALED, State.CONNECTING)
        ],
    State.CONNECTING: [
        (Trigger.HUNG_UP, State.ON_HOLD),
        (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
    State.CONNECTED: [
        (Trigger.LEFT_MESSAGE, State.ON_HOOK),
        (Trigger.HUNG_UP, State.ON_HOOK),
        (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
        ],
    State.ON_HOLD: [
        (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
        (Trigger.HUNG_UP, State.ON_HOOK)
        ]
    }


def main():
    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f'The phone is currently {state}')

        for i in range(len(RULES[state])):
            trigger = RULES[state][i][0]
            print(f'{i}:{trigger}')
        
        index = int(input('Select a trigger: '))
        state = RULES[state][index][1]
    
    print('Zawieszono połączenie')

if __name__ == "__main__":
    main()