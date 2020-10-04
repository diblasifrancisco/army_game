from army_game.mixins.coin_transaction import CoinTransactionMixin

from army_game.models.battle import Battle


class BattleBackend(CoinTransactionMixin):

    @classmethod
    def _process_tie(cls, attacking_army, attacked_army):
        attacking_army.army_branches.sort(
            key=lambda x: x.points,
            reverse=True,
        )[:1].remove()
        attacking_army.attacked_army.sort(
            key=lambda x: x.points,
            reverse=True,
        )[:1].remove()

    @classmethod
    def _process_looser(cls, looser):
        branches_to_loose = looser.army_branches.sort(
            key=lambda x: x.points,
            reverse=True,
        )[:2]
        branches_to_loose[0].remove()
        branches_to_loose[1].remove()

    @classmethod
    def fight(cls, attacking_army, attacked_army):
        """
        The winner army earns 100 coins
        The looser army lost 2 army branches with the maximum points
        If it's a tie, both armies lost a branch tha has most of the points.

        """
        winner = None
        is_a_tie = False
        amount = 100
        looser = None

        if attacking_army > attacked_army:
            winner = attacking_army
            looser = attacked_army

        elif attacking_army < attacked_army:
            winner = attacked_army
            looser = attacking_army

        else:
            is_a_tie = True
            amount = 0

        if is_a_tie:
            BattleBackend._process_tie(
                attacking_army,
                attacked_army,
            )
        else:
            BattleBackend._process_looser(
                looser,
            )

        battle = Battle(
            attacking_army=attacking_army,
            attacked_army=attacked_army,
            winner_army=winner,
            is_a_tie=is_a_tie,
            amount=amount,
            army=winner,
        )

        if amount > 0:
            BattleBackend.process_coin_transaction(
                battle,
            )

        return winner
