from army_game.models.transformation import Transformation
from army_game.constants import (
    BRANCH_TO_LEVEL,
    LEVEL_TO_BRANCH,
    TRASFORMATION_BRANCH_COST,
)
from army_game.mixins.coin_transaction import CoinTransactionMixin

from army_game.exceptions import (
    BranchUpgradeNotAvailable,
    NotEnoughCoins,
)


class TransformationBackend(CoinTransactionMixin):

    @classmethod
    def transform_branch(cls, army_branch):
        """
        It tries to train the branch to the next level if possible
        It returns the transformation created.

        """
        current_number_level = BRANCH_TO_LEVEL[army_branch.branch_type]
        next_branch = LEVEL_TO_BRANCH.get(current_number_level + 1)
        if not next_branch:
            raise BranchUpgradeNotAvailable(
                "This branch has reached the maximum level.",
            )
        next_level_cost = TRASFORMATION_BRANCH_COST[
            next_branch
        ]

        if army_branch.army.coins < next_level_cost:
            raise NotEnoughCoins("Army has not enought founds.")

        army_branch.branch_type = next_branch
        transformation = Transformation(
            amount=next_level_cost,
            army_branch=army_branch,
            old_branch_type=LEVEL_TO_BRANCH[current_number_level],
            new_branch_type=next_branch,
        )

        coin_transaction = TransformationBackend.process_coin_transaction(
            transformation,
        )

        return transformation, army_branch, coin_transaction
