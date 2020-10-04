class Army():

    def __init__(self, civilization):
        self.army_branches = []
        self.coins = 1000
        self.civilization = civilization

    def points(self):
        return sum(branch.points for branch in self.army_branches)
