from objects.singleton import Singleton
from objects.static_object import StaticSingleton

class EngineSettings(StaticSingleton):
    __is_running = True

    def is_running(self):
        return EngineSettings.__is_running

    def set_running(self, val):
        EngineSettings.__is_running = val

