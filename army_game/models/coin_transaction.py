from datetime import datetime


class CoinTransaction():

    def __init__(self, army, coins, created, object_reference):
        self.army = army
        self.coins = coins
        self.created = datetime.now()
        self.object_reference = object_reference
