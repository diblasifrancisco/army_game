import random

from army_game.backend.army_branch import ArmyBranchBackend
from army_game.backend.battle import BattleBackend
from army_game.backend.training import TrainingBackend
from army_game.backend.transformation import TransformationBackend

from army_game.models import (
    Army,
    Civilization,
)


class Game(object):

    def __init__(self):
        """
        Creates civilizations and armies based on the data store on the constants file

        """
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

        self.armies = [
            english_army,
            chinese_army,
            byzantine_army,
        ]

    def play(self):
        """
        It simulates a game by choosing two armies randomly

        """
        army_one = random.choice(self.armies)
        self.armies.remove(army_one)
        army_two = random.choice(self.armies)
        self.armies.remove(army_two)

        print(
            "{} vs {}".format(
                army_one.civilization.name,
                army_two.civilization.name,
            ),
        )

        # simulate training and transforamations
        for x in range(5):
            # TODO update list of branches for each army on every transformation and training, also after a battle
            branch_selected_to_be_trained_army_one = random.randint(0, len(army_one.army_branches)-1)
            branch_selected_to_be_trained_army_two = random.randint(0, len(army_two.army_branches)-1)

            TrainingBackend.train_branch(army_one.army_branches[branch_selected_to_be_trained_army_one])
            TrainingBackend.train_branch(army_two.army_branches[branch_selected_to_be_trained_army_two])

            archers_and_pikeman_army_one = [branch for branch in army_one.army_branches if branch.branch_type != 'Chivalry']
            archers_and_pikeman_army_two = [branch for branch in army_two.army_branches if branch.branch_type != 'Chivalry']

            branch_selected_to_be_transformed_army_one = random.randint(0, len(archers_and_pikeman_army_one)-1)
            branch_selected_to_be_transformed_army_two = random.randint(0, len(archers_and_pikeman_army_two)-1)

            TransformationBackend.transform_branch(archers_and_pikeman_army_one[branch_selected_to_be_transformed_army_one])
            TransformationBackend.transform_branch(archers_and_pikeman_army_two[branch_selected_to_be_transformed_army_two])

        battle = BattleBackend.fight(
            army_one,
            army_two,
        )

        if battle.is_a_tie:
            print("It's a tie!")
        else:
            print(
                "The winner is the army from the {} civilation!".format(
                    battle.winner_army.civilization.name,
                )
            )
            print(
                "{} {} points vs {} {} points".format(
                    army_one.civilization.name,
                    army_one.points,
                    army_two.civilization.name,
                    army_two.points,
                ),
            )


if __name__ == '__main__':
    Game().play()
