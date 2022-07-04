from console.command.argument import Argument

class ArgumentContainer:
    def __init__(self, arguments = None, optional_arguments = None) -> None:
        self.arguments : list[Argument] = arguments or []
        self.optional_arguments : list[Argument] = optional_arguments or []

    def min_arguments(self) -> int:
        return len(self.arguments)
    
    def max_arguments(self) -> int:
        return len(self.arguments) + len(self.optional_arguments)

    def fill(self, args):
        i = 0
        min = self.min_arguments()

        while len(args) > 0:
            arg = args.pop(0)

            if i < len(self.arguments):
                self.arguments[i].fill(arg)
            else:
                self.optional_arguments[i - min].fill(arg)
    
    def clear(self):
        for arg in self.arguments + self.optional_arguments:
            arg.value = None