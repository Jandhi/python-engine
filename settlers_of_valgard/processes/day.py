from events.game_event import GameEvent

class TimePassEvent(GameEvent):
    def __init__(self) -> None:
        super().__init__()

class DayEndEvent(TimePassEvent):
    def __init__(self, old_day, new_day) -> None:
        super().__init__()
        self.old_day = old_day
        self.new_day = new_day