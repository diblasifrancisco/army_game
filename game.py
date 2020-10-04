from army_game.backend.army_branch import ArmyBranchBackend
from army_game.models import (
    Army,
    Civilization,
)


class Game(object):

    def play(self):
        # initial data
        english_civilization = Civilization(name='English')
        english_army = Army(
            civilization=english_civilization,
        )
        english_army.army_branches = ArmyBranchBackend.create_branches_for_army(
            army=english_army,
        )

        chinese_civilization = Civilization(name='Chinese')
        chinese_army = Army(
            civilization=chinese_civilization,
        )
        chinese_army.army_branches = ArmyBranchBackend.create_branches_for_army(
            army=chinese_army,
        )

        byzantine_civilization = Civilization(name='Byzantine')
        byzantine_army = Army(
            civilization=byzantine_civilization,
        )
        byzantine_army.army_branches = ArmyBranchBackend.create_branches_for_army(
            army=byzantine_army,
        )


if __name__ == '__main__':
    Game().play()
