from army_game.models.transaction import Transaction


class Transformation(Transaction):

    def __init__(self, army, cost_coins, old_branch, new_branch):
        super().__init__('transformation', cost_coins)
        self.army = army
        self.old_branch = old_branch
        self.new_branch = new_branch
