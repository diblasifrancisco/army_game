from army_game.constants import TRAINING_FORCE_POINTS_COST
from army_game.models.training import Training
from army_game.mixins.coin_transaction import CoinTransactionMixin


class TransformationBackend(CoinTransactionMixin):

    @classmethod
    def train_branch(cls, army_branch):
        training_cost_points = TRAINING_FORCE_POINTS_COST[
            army_branch.branch_type,
        ]
        cost = training_cost_points['cost']
        if army_branch.army.coins < cost:
            raise Exception("This army {} has not enought founds.".format(
                army_branch.army.name,
                ),
            )

        army_branch.points = training_cost_points['points']

        training = Training(
            army=army_branch.army,
            cost_coins=cost,
            force_points=training_cost_points['points'],
        )

        TransformationBackend.process_coin_transaction(
            training,
        )

        return training
