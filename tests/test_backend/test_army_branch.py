from army_game.backend.army_branch import ArmyBranchBackend


class TestArmyBranch:

    def _get_unit_from_branch(self, army_branches, branch_type):
        return [branch for branch in army_branches if branch.branch_type == branch_type]


    def test_create_branches_for_english_army(self, english_civilization, english_army):
        army_branches = ArmyBranchBackend.create_branches_for_army(
            army=english_army,
        )
        archer = self._get_unit_from_branch(army_branches, 'Archer')
        pikeman = self._get_unit_from_branch(army_branches, 'Pikeman')
        chivalry = self._get_unit_from_branch(army_branches, 'Chivalry')

        assert len(army_branches) == 30
        assert len(archer) == 10
        assert len(pikeman) == 10
        assert len(chivalry) == 10


    def test_create_branches_for_chinese_army(self, chinese_civilization, chinese_army):
        army_branches = ArmyBranchBackend.create_branches_for_army(
            army=chinese_army,
        )
        archer = self._get_unit_from_branch(army_branches, 'Archer')
        pikeman = self._get_unit_from_branch(army_branches, 'Pikeman')
        chivalry = self._get_unit_from_branch(army_branches, 'Chivalry')

        assert len(army_branches) == 29
        assert len(archer) == 2
        assert len(pikeman) == 25
        assert len(chivalry) == 2


    def test_create_branches_for_byzantine_army(self, byzantine_civilization, byzantine_army):
        army_branches = ArmyBranchBackend.create_branches_for_army(
            army=byzantine_army,
        )
        archer = self._get_unit_from_branch(army_branches, 'Archer')
        pikeman = self._get_unit_from_branch(army_branches, 'Pikeman')
        chivalry = self._get_unit_from_branch(army_branches, 'Chivalry')

        assert len(army_branches) == 28
        assert len(archer) == 5
        assert len(pikeman) == 8
        assert len(chivalry) == 15
