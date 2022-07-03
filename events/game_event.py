from inspect import getmro

__event_listeners = {}

def initialize_events():
    global __event_listeners
    __event_listeners = {}

def get_event_listeners():
    return __event_listeners

def add_listener(type, listener, filter=None):
    if type not in __event_listeners:
        __event_listeners[type] = []
    
    __event_listeners[type].append((listener, filter))

class GameEvent:
    def __init__(self) -> None:
        self.received = []
    
    def send(self):
        types = getmro(type(self))

        for event_type in types:
            if event_type in get_event_listeners():
                for listener, filter in get_event_listeners()[event_type]:
                    if listener in self.received:
                        continue

                    if filter is None or filter(self):
                        self.received.append(listener)
                        listener(self)
    
    def send_and_return(self):
        self.send()
        return self