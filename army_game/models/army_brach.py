ARMY_STATUS = {
    'ACTIVE': 'ACTIVE',
    'INACTIVE': 'INACTIVE',
}


class ArmyBranch():

    def __init__(self, branch_type, army, points):
        self.branch_type = branch_type
        self.army = army
        self.points = points
        self.status = ARMY_STATUS['ACTIVE']

    def remove(self):
        self.status = ARMY_STATUS['INACTIVE']
