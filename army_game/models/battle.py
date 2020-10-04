from datetime import datetime

from army_game.models.transaction import Transaction


class Battle(Transaction):

    def __init__(
        self,
        attacking_army,
        attacked_army,
        winner_army,
        is_a_tie,
        amount,
    ):
        super().__init__('battle', amount, winner_army)
        self.attacking_army = attacking_army
        self.attacked_army = attacked_army
        self.winner_army = winner_army
        self.is_a_tie = is_a_tie
        self.created = datetime.now()
