from objects.singleton import Singleton

class EngineSettings(Singleton):
    __is_running = True

    class Schema(Singleton.Schema):
        is_static = True

    def is_running(self):
        return EngineSettings.__is_running

    def set_running(self, val):
        EngineSettings.__is_running = val

