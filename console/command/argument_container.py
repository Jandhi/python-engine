from console.command.argument import Argument

class ArgumentContainer:
    def __init__(self, name, arguments = None, optional_arguments = None) -> None:
        self.arguments : list[Argument] = arguments or []
        self.optional_arguments : list[Argument] = optional_arguments or []
        self.name = name

    def min_arguments(self) -> int:
        return len(self.arguments)
    
    def max_arguments(self) -> int:
        return len(self.arguments) + len(self.optional_arguments)

    def fill(self, args):
        i = 0
        min = self.min_arguments()

        if len(args) < min:
            raise ValueError(f'{self.name} requires at least {min} arguments')

        while len(args) > 0:
            arg = args.pop(0)

            if i < len(self.arguments):
                self.arguments[i].fill(arg)
            elif i - min >= len(self.optional_arguments):
                raise ValueError(f'{self} can only take up to {max} arguments')
            else:
                self.optional_arguments[i - min].fill(arg)
            
            i += 1
    
    def clear(self):
        for arg in self.arguments + self.optional_arguments:
            arg.value = None