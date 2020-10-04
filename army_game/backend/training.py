from army_game.constants import TRAINING_FORCE_POINTS_COST
from army_game.models.training import Training
from army_game.mixins.coin_transaction import CoinTransactionMixin

from army_game.exceptions import NotEnoughCoins


class TrainingBackend(CoinTransactionMixin):
    """
    It tries to train the branch if possible
    It returns the training created, the branch trained and
    the transaction generated

    """
    @classmethod
    def train_branch(cls, army_branch):
        training_cost_points = TRAINING_FORCE_POINTS_COST[army_branch.branch_type]
        cost = training_cost_points['cost']
        if army_branch.army.coins < cost:
            raise NotEnoughCoins("This army has not enought founds.")

        army_branch.points += training_cost_points['points']

        training = Training(
            army_branch=army_branch,
            cost_coins=cost,
            force_points=training_cost_points['points'],
        )

        coin_transaction = TrainingBackend.process_coin_transaction(
            training,
        )

        return training, army_branch, coin_transaction
