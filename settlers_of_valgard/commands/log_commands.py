
from console.command.command import Command
from console.command.argument import Argument, IntegerArgument
from console.command.scopes import IN_GAME
from console.command.tag import Tag
from console.error import print_error
from objects.game_object import find_object
from objects.query import Query
from settlers_of_valgard.logger.logging_level import LogDetailLevel
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.logger.logger import Logger
from settlers_of_valgard.player_info import PlayerInfo

log_detail_level_argument = Argument('detail level', 'the level of detail of logs you want to see')
log_detail_tag = Tag('-detail', 'the level of detail of the logs', ['-d'], [log_detail_level_argument])
log_day_argument = IntegerArgument('day', 'the day whose logs you want to see')
def log_execute(cmd):
    day = log_day_argument.value or find_object(Settlement).day
    logger = Logger.instance
    level = None

    detail_arg = log_detail_level_argument.value
    if detail_arg is not None:
        level = Query(LogDetailLevel).filter(lambda lvl : lvl.name.lower() == detail_arg.lower()).first()
    else:
        level = Query(PlayerInfo).first().logging_level

    if day not in logger.contents:
        print_error(f'There is no log for day {day}')
    else:
        for msg, lvl in logger.contents[day]:
            if lvl >= level:
                print(msg)

log_command = Command(
    'log',
    'displays the log of the current or a given day',
    log_execute,
    optional_arguments=[log_day_argument],
    scope=IN_GAME
)