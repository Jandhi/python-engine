class ArgumentContainer:
    def __init__(self, arguments = None, optional_arguments = None) -> None:
        self.arguments = arguments or []
        self.optional_arguments = optional_arguments or []