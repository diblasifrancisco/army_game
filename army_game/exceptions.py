class NotEnoughCoins(Exception):
    """
    Not enough coins to make a transaction

    """
    pass


class BranchUpgradeNotAvailable(Exception):
    """
    Branch cannot be upgraded

    """
    pass


class NotEnoughArmyBranches(Exception):
    """
    There's not enough branches

    """
    pass
