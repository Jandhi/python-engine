from console.colored_string import color
from console.command.command import Command
from console.error import cerror
from console.palette import Palette
from objects.game_object import get_objects

class CommandManager:
    def get_commands(self) -> list[Command]:
        return get_objects(Command)

    def process_input(self, input) -> None:
        args = self.split(input)

        if len(args) == 0:
            return

        command_name = args.pop(0)
        command = self.find_command(command_name)

        if command is None:
            cerror(f'No command with name "{color(command_name, Palette.INPUT_COLOR)}"')
            return
        
        try:
            command.fill(args)
        except ValueError as v:
            print(v)
        
        command.execute(command)
        command.clear()

    def find_command(self, name) -> Command:
        commands = self.get_commands()

        for command in commands:
            if command.name == name:
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
