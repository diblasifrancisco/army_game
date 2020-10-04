import pytest

from army_game.backend.army_branch import ArmyBranchBackend
from army_game.backend.battle import BattleBackend

from army_game.exceptions import NotEnoughArmyBranches


class TestBattleBackend:

    def test_battle_not_enough_branches(self, english_army, chinese_army):
        with pytest.raises(NotEnoughArmyBranches):
            BattleBackend.fight(
                english_army,
                chinese_army,
            )

    def test_battle(self, english_army, chinese_army):
        english_army.army_branches = ArmyBranchBackend.create_branches_for_army(
            army=english_army,
        )
        chinese_army.army_branches = ArmyBranchBackend.create_branches_for_army(
            army=chinese_army,
        )
        battle = BattleBackend.fight(
            english_army,
            chinese_army,
        )

        assert battle.winner_army == english_army
        assert battle.is_a_tie == False
        # the loose lost two branches
        assert len(battle.attacked_army.get_active_army_branches()) == 27

    def test_battle_tie(self, english_army, chinese_army):
        english_army.army_branches = ArmyBranchBackend.create_branches_for_army(
            army=english_army,
        )
        chinese_army.army_branches = ArmyBranchBackend.create_branches_for_army(
            army=english_army,
        )
        battle = BattleBackend.fight(
            english_army,
            chinese_army,
        )

        assert battle.winner_army == None
        assert battle.is_a_tie == True
        # both loose one branch
        assert len(battle.attacking_army.get_active_army_branches()) == 29
        assert len(battle.attacked_army.get_active_army_branches()) == 29
