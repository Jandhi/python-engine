from noise.seed import get_game_seed
from settlers_of_valgard.building.prototype.workplace import Workplace
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.resource.bundle import Bundle
from settlers_of_valgard.resource.resource import send_to_stockpile
from settlers_of_valgard.settler.settler import Settler
from noise.dice import highest

class Harvester(Workplace):
    def __init__(self, name, color, skill, basket : list[Bundle], workers=None) -> None:
        super().__init__(name, color, workers)

        self.relevant_skill = skill
        self.basket = basket

    def __work(self, worker : Settler, settlement):
        lvl = worker.get_skill_level(self.relevant_skill)
        roll = lvl.get_dice().highest(get_game_seed() * settlement.day * worker)
        gain = self.basket[roll - 1].copy()

        send_to_stockpile(gain) 