from army_game.mixins.coin_transaction import CoinTransactionMixin

from army_game.models import Battle

from army_game.exceptions import NotEnoughArmyBranches


class BattleBackend(CoinTransactionMixin):

    @classmethod
    def _process_tie(cls, attacking_army_branches, attacked_army_branches):
        attacking_army_branches[0].remove()
        attacked_army_branches[0].remove()

    @classmethod
    def _process_loser(cls, loser_branches):
        loser_branches[0].remove()
        loser_branches[1].remove()

    @classmethod
    def fight(cls, attacking_army, attacked_army):
        """
        The army that has more points wins, and earns 100 coins.
        The loser army lost 2 army branches with the highest score.
        If it's a tie, both armies lost a branch with the highest score.

        """
        winner = None
        is_a_tie = False
        amount = 100
        loser_branches = None

        attacking_army_branches = sorted(attacking_army.get_active_army_branches(), key=lambda x: x.points)
        attacked_army_branches = sorted(attacked_army.get_active_army_branches(), key=lambda x: x.points)

        # armies should have at least 2 branches to fight
        if (
            not attacking_army_branches or
            len(attacking_army_branches) <= 2 or
            not attacked_army_branches or
            len(attacked_army_branches) <= 2
        ):
            raise NotEnoughArmyBranches("There is no enough branches to start a battle")

        if attacking_army.points > attacked_army.points:
            winner = attacking_army
            loser_branches = attacked_army_branches

        elif attacking_army.points < attacked_army.points:
            winner = attacked_army
            loser_branches = attacking_army_branches

        else:
            is_a_tie = True
            amount = 0

        if is_a_tie:
            BattleBackend._process_tie(
                attacking_army_branches,
                attacked_army_branches,
            )
        else:
            BattleBackend._process_loser(
                loser_branches,
            )

        battle = Battle(
            attacking_army=attacking_army,
            attacked_army=attacked_army,
            winner_army=winner,
            is_a_tie=is_a_tie,
            amount=amount,
        )
        attacking_army.battles.append(battle)
        attacked_army.battles.append(battle)

        if amount > 0:
            BattleBackend.process_coin_transaction(
                battle,
            )

        return battle
