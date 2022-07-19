from events.game_event import GameEvent

class TimePassEvent(GameEvent):
    def __init__(self, current_day) -> None:
        super().__init__()
        self.current_day = current_day

class DayStartEvent(TimePassEvent):
    def __init__(self, current_day) -> None:
        super().__init__(current_day)

class DaytimeStartEvent(TimePassEvent):
    def __init__(self, current_day) -> None:
        super().__init__(current_day)

class DaytimeEndEvent(TimePassEvent):
    def __init__(self, current_day) -> None:
        super().__init__(current_day)

class EveningStartEvent(TimePassEvent):
    def __init__(self, current_day) -> None:
        super().__init__(current_day)

class EveningEndEvent(TimePassEvent):
    def __init__(self, current_day) -> None:
        super().__init__(current_day)

class NightStartEvent(TimePassEvent):
    def __init__(self, current_day) -> None:
        super().__init__(current_day)

class NightEndEvent(TimePassEvent):
    def __init__(self, current_day) -> None:
        super().__init__(current_day)

class DayEndEvent(TimePassEvent):
    def __init__(self, current_day, new_day) -> None:
        super().__init__(current_day)
        self.new_day = new_day

def pass_day(current_day):
    for ev in (
        DayStartEvent, 
        DaytimeStartEvent, 
        DaytimeEndEvent,
        EveningStartEvent,
        EveningEndEvent,
        NightStartEvent,
        NightEndEvent
    ):
        ev(current_day).send()

    DayEndEvent(current_day, current_day + 1).send()