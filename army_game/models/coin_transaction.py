from datetime import datetime


class CoinTransaction():

    def __init__(self, army, amount, transaction_type, object_reference):
        self.army = army
        self.amount = amount
        self.created = datetime.now()
        self.transaction_type = transaction_type
        self.object_reference = object_reference
