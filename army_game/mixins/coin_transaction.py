from army_game.models import CoinTransaction

INCREASE_BALANCE_TRANSACTIONS = [
    'battle',
]

DECREASE_BALANCE_TRANSACTIONS = [
    'transformation',
    'training',
]


class CoinTransactionMixin():
    """
    Mixin for all the events or transactions that have an impact on the coin balance.

    """
    @classmethod
    def process_coin_transaction(cls, transaction):
        if transaction.transaction_type in INCREASE_BALANCE_TRANSACTIONS:
            transaction.army.coins += transaction.amount

        elif transaction.transaction_type in DECREASE_BALANCE_TRANSACTIONS:
            transaction.army.coins -= transaction.amount

        else:
            raise Exception("This operation is not supported.")

        return CoinTransaction(
            transaction_type=transaction.transaction_type,
            army=transaction.army,
            amount=transaction.amount,
            object_reference=transaction,
        )
