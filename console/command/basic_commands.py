from os import system
from console.colored_string import color
from console.command.command import Command
from console.command.command_manager import CommandManager
from console.command.query_command import QueryCommand
from console.command.tag import Tag
from console.palette import Palette
from console.title import title
from console.verification import get_verification
from engine_settings import EngineSettings
from objects.game_object import find_object

force_quit_tag = Tag('-f', 'forces the game to quit')
def Quit(cmd):
    if force_quit_tag.used or get_verification("Do you really want to exit the game?"):
        find_object(EngineSettings).set_running(False)
        find_object(EngineSettings).set_running(False)
        print("Goodbye!")

Command(
    "quit",
    "Quits the game",
    Quit,
    ['q', 'Quit', 'exit', 'end'],
    tags=[force_quit_tag],
)

def display_tag(tag : Tag):
    s = f'{color(tag.name, Palette.BLUE)}'

    for arg in tag.arguments:
        s = f'{s} {color(f"<{arg.name}>", Palette.ORANGE)}'
    for arg in tag.optional_arguments:
        s = f'{s} {color(f"({arg.name})", Palette.YELLOW)}'

    s = f'{s}\n'

    for arg in tag.arguments:
        s = f'{s}\t{color(arg.name, Palette.ORANGE)} - {arg.description}\n'

    for arg in tag.optional_arguments:
        s = f'{s}\t{color(arg.name, Palette.YELLOW)} - {arg.description}\n'    
    
    return s

def display_command(cmd : Command):
    s = f'{title(cmd)}\n'
    
    usage = f'{cmd}'
    for arg in cmd.arguments:
        usage = f'{usage} {color(f"<{arg.name}>", Palette.ORANGE)}'
    for arg in cmd.optional_arguments:
        usage = f'{usage} {color(f"({arg.name})", Palette.YELLOW)}'

    s = f'{s}Usage: {usage}\n'

    if len(cmd.aliases) > 0:
        s = f'{s}Aliases: '

        for alias in cmd.aliases:
            alias_text = f'"{alias}"'
            s = f'{s} {color(alias_text, Palette.INPUT_COLOR)},'
        
        s = f'{s[:-1]}\n'

    s = f'{s}{cmd.description}\n'

    if len(cmd.arguments) > 0 or len(cmd.optional_arguments):
        s = f'{s}\n{color("ARGUMENTS", Palette.UNDERLINE)}:\n'

        for arg in cmd.arguments:
            s = f'{s}{color(arg.name, Palette.ORANGE)} - {arg.description}\n'

        for arg in cmd.optional_arguments:
            s = f'{s}{color(arg.name, Palette.YELLOW)} - {arg.description}\n'
    
    if len(cmd.tags) > 0:
        s = f'{s}\n{color("TAGS", Palette.UNDERLINE)}:\n'

        for tag in cmd.tags:
            s = f'{s}{display_tag(tag)}\n'
        
    return s[:-1]

QueryCommand(
    'commands',
    'lists available commands',
    Command,
    display_command,
    aliases=['cmd', 'command', 'cmds']
)

Command(
    'clear',
    'clears the screen',
    lambda cmd : system('cls'),
    aliases=['clr', 'cls']
)

def clearmode(cmd):
    manager : CommandManager = find_object(CommandManager)
    manager.clear_before_command = not manager.clear_before_command

    if manager.clear_before_command:
        print(f'Clear mode is now {color("ON", Palette.GREEN)}')
    else:
        print(f'Clear mode is now {color("OFF", Palette.RED)}')

Command(
    'clearmode',
    'toggles whether the game clears the screen before running commands',
    clearmode,
    aliases=['cm', 'clmd']
)