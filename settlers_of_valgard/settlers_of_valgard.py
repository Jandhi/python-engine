from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.settler.settler import Settler
import settlers_of_valgard.commands.work_commands
import settlers_of_valgard.commands.settler_commands
from settlers_of_valgard.processes.hunting.hunting import Hunting
import settlers_of_valgard.commands.hunger_commands 

s = Settlement()

s.settlers = [
    Settler('Bjorn'),
    Settler('Norn'),
    Settler('Vorn')
]

s.settlers[2].add_xp(Hunting, 100)



