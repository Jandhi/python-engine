from events.game_event import GameEvent, initialize_events, add_listener

initialize_events()

class TestEvent(GameEvent):
    def __init__(self, hidden) -> None:
        super().__init__()

        self.hidden = hidden

received = ''

def filter(event):
    if not isinstance(event, TestEvent):
        return True

    return not event.hidden

def listen(event):
    global received
    received += 'true'

add_listener(GameEvent, listen, filter)

ev = TestEvent(False)
ev.send()
ev.send()
TestEvent(True).send()

assert(received == 'true')