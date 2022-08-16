from settlers_of_valgard.logger.logger import Logger
from settlers_of_valgard.player_info import PlayerInfo
from settlers_of_valgard.processes.day import pass_day
from settlers_of_valgard.resource.food import Meat
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.settler.settler import Settler
import settlers_of_valgard.commands.work_commands
import settlers_of_valgard.commands.settler_commands
from settlers_of_valgard.processes.hunting.hunting import Hunting
import settlers_of_valgard.commands.hunger_commands 
import settlers_of_valgard.commands.log_commands

s = Settlement()
PlayerInfo()
Logger()

s.stockpile.add(Meat, 2)

s.settlers = [
    Settler('Bjorn'),
    Settler('Norn'),
    Settler('Vorn')
]

s.settlers[2].add_xp(Hunting, 100)

pass_day(0)


