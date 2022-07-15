from events.game_event import GameEvent

class SoVEvent(GameEvent):
    pass

class BlockableEvent(SoVEvent):
    def __init__(self) -> None:
        super().__init__()

        self.blocked = False
    
    def send_is_success(self) -> bool:
        self.send()

        return not self.blocked