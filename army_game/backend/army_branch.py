from army_game.models import ArmyBranch
from army_game.constants import (
    BRANCH_POINTS,
    CIVILIZATIONS,
)


class ArmyBranchBackend():

    @classmethod
    def create_branches_for_army(cls, army):
        """
        Creates all army branches depending on the quanty defined for each civilization

        """
        army_branches = []
        civilization_name = army.civilization.name
        quantity_per_branch = CIVILIZATIONS[civilization_name]
        for branch_type, quantity in quantity_per_branch.items():
            for n in range(quantity):
                army_branches.append(
                    ArmyBranch(
                        army=army,
                        points=BRANCH_POINTS[branch_type],
                        branch_type=branch_type,
                    )
                )
        return army_branches
