from army_game.models.transaction import Transaction


class Training(Transaction):

    def __init__(self, army_branch, cost_coins, force_points):
        super().__init__('training', cost_coins, army_branch.army)
        self.army_branch = army_branch
        self.cost_coins = cost_coins
        self.force_points = force_points
