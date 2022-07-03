

__is_running = True

def is_running():
    return __is_running

def set_running(val):
    global __is_running
    __is_running = val

