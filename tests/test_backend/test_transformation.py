import pytest

from army_game.backend.transformation import TransformationBackend
from army_game.constants import (TRAINING_FORCE_POINTS_COST, TRASFORMATION_BRANCH_COST)

from army_game.exceptions import (
    BranchUpgradeNotAvailable,
    NotEnoughCoins,
)


class TestTransformationBackend:

    def test_transformation_not_possible_maximum_level(self, chivalry_army_branch):
        with pytest.raises(BranchUpgradeNotAvailable):
            TransformationBackend.transform_branch(chivalry_army_branch)

    def test_transformation_not_enough_coins(self, archer_army_branch):
        archer_army_branch.army.coins = 0
        with pytest.raises(NotEnoughCoins):
            TransformationBackend.transform_branch(archer_army_branch)

    def test_transformation_branch_successfully(self, archer_army_branch):
        transformation, army_branch_transformed, coin_transaction = TransformationBackend.transform_branch(
            archer_army_branch,
        )

        assert transformation.new_branch_type == 'Pikeman'
        assert transformation.amount == TRASFORMATION_BRANCH_COST['Pikeman']
        assert transformation.old_branch_type == 'Archer'
        assert transformation.army_branch == archer_army_branch

        assert army_branch_transformed.branch_type == 'Pikeman'
        assert army_branch_transformed.points == TRAINING_FORCE_POINTS_COST['Pikeman']['points']
