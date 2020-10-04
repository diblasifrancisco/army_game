from army_game.models.transaction import Transaction


class Training(Transaction):

    def __init__(self, army, cost_coins, force_points):
        super().__init__('training', cost_coins)
        self.army = army
        self.cost_coins = cost_coins
        self.force_points = force_points
