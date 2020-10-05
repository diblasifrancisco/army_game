class Army():

    def __init__(self, civilization):
        self.army_branches = []
        self.battles = []
        self.coins = 1000
        self.civilization = civilization

    @property
    def points(self):
        return sum(branch.points for branch in self.army_branches if branch.status == 'ACTIVE')

    def get_active_army_branches(self):
        return [branch for branch in self.army_branches if branch.status == 'ACTIVE']
