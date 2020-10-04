from army_game.models.transformation import Transformation
from army_game.constants import (
    BRANCH_TO_LEVEL,
    LEVEL_TO_BRANCH,
    TRASFORMATION_BRANCH_COST,
)
from army_game.mixins.coin_transaction import CoinTransactionMixin


class TransformationBackend(CoinTransactionMixin):

    @classmethod
    def transform_branch(cls, army_branch):
        """
        It tries to train the branch to the next level if possible

        """
        current_number_level = BRANCH_TO_LEVEL[army_branch.branch_type]
        next_branch = LEVEL_TO_BRANCH.get(current_number_level + 1)
        if not next_branch:
            raise Exception("This branch has reached the maximum level.")
        next_level_cost = TRASFORMATION_BRANCH_COST[
            LEVEL_TO_BRANCH[next_branch]
        ]

        if army_branch.army.coins < next_level_cost:
            raise Exception("This army {} has not enought founds.".format(
                army_branch.army.name,
                ),
            )

        army_branch.brach_type = next_branch
        transformation = Transformation(
            army=army_branch.army,
            cost_coins=next_level_cost,
            old_branch=army_branch.branch_type,
            new_branch=next_branch,
        )

        TransformationBackend.process_coin_transaction(
            transformation,
        )

        return transformation
