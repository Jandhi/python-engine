from events.game_event import GameEvent, initialize_events, register_listener

initialize_events()

class TestEvent(GameEvent):
    def __init__(self, hidden) -> None:
        super().__init__()

        self.hidden = hidden

received = ''

def filter(event):
    return not event.hidden

def listen(event):
    global received
    received += 'true'

register_listener(TestEvent, listen, filter)

ev = TestEvent(False)
ev.send()
ev.send()
TestEvent(True).send()

assert(received == 'true')