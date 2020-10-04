import pytest

from army_game.backend.training import TrainingBackend
from army_game.constants import TRAINING_FORCE_POINTS_COST

from army_game.exceptions import NotEnoughCoins


class TestTrainingBackend:

    def test_training_not_enough_coins(self, archer_army_branch):
        archer_army_branch.army.coins = 0
        with pytest.raises(NotEnoughCoins):
            TrainingBackend.train_branch(
                archer_army_branch,
            )

    def test_train_archers_sucessfully(self, archer_army_branch):
        initial_army_points = archer_army_branch.army.points
        initial_army_branch_points = archer_army_branch.points

        training, army_branch_trained, coin_transaction = TrainingBackend.train_branch(
            archer_army_branch,
        )

        assert training.army_branch == archer_army_branch
        assert training.cost_coins == TRAINING_FORCE_POINTS_COST['Archer']['cost']
        assert training.force_points == TRAINING_FORCE_POINTS_COST['Archer']['points']

        assert army_branch_trained.army.points == (initial_army_points + training.force_points)
        assert army_branch_trained.points == (initial_army_branch_points + training.force_points)

        assert coin_transaction.transaction_type == 'training'
        assert coin_transaction.army == archer_army_branch.army
        assert coin_transaction.amount == TRAINING_FORCE_POINTS_COST['Archer']['cost']
        assert coin_transaction.object_reference == training
