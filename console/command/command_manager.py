from os import system
from console.colored_string import color
from console.command.command import Command
from console.command.scopes import ENGINE_MENU, GLOBAL
from console.error import print_error
from console.palette import Palette
from objects.query import Query
from objects.static_object import StaticSingleton

class CommandManager(StaticSingleton):
    def __init__(self) -> None:
        super().__init__()
        self.scopes = [GLOBAL, ENGINE_MENU]
        self.clear_before_command = True
        self.keep_next = False

    def get_commands(self) -> list[Command]:
        return Query(Command).filter(lambda cmd : cmd.scope in self.scopes).all()

    def process_input(self, input) -> None:
        args = self.split(input)
        args_copy : list = args.copy()

        if len(args) == 0:
            return

        command_name = args.pop(0)
        command = self.find_command(command_name)

        if command is None:
            cname = f'"{command_name}"'
            print_error(f'No command with name {color(cname, Palette.INPUT_COLOR)}')
            return
        
        try:
            command.fill(args)
        except ValueError as v:
            print(v)
            return command.clear()
        
        if self.clear_before_command and not self.keep_next:
            system('cls')
            args_copy[0] = command.text

            print(' '.join(args_copy))
        
        command.execute(command)
        command.clear()

        self.keep_next = False

    def find_command(self, name) -> Command:
        commands = self.get_commands()

        for command in commands:
            if command.text == name:
                return command
        
        for command in commands:
            if name in command.aliases:
                return command

    def split(self, str) -> list[str]:
        start = 0
        end = 0
        in_quote = False
        parts = []

        while end < len(str):
            if str[end:end + 1] == '"':
                if in_quote:
                    parts.append(str[start:end])
                    start = end + 1
                    in_quote = False
                else:
                    parts.append(str[start:end])
                    start = end + 1
                    in_quote = True
            
            if str[end:end + 1] == ' ' and not in_quote:
                parts.append(str[start:end])
                start = end + 1
            
            end += 1

        parts.append(str[start:end])
        start = end + 1

        parts = list(filter(lambda x : x != '', parts))
    
        return parts
