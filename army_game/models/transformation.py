from army_game.models.transaction import Transaction


class Transformation(Transaction):

    def __init__(self, army_branch, amount, old_branch_type, new_branch_type):
        super().__init__('transformation', amount, army_branch.army)
        self.army_branch = army_branch
        self.old_branch_type = old_branch_type
        self.new_branch_type = new_branch_type
