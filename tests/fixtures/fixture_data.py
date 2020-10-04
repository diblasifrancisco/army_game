import pytest

from army_game.models.army import Army
from army_game.models.civilization import Civilization


@pytest.fixture()
def english_civilization():
    return Civilization(
        name='English',
    )


@pytest.fixture()
def chinese_civilization():
    return Civilization(
        name='Chinese',
    )


@pytest.fixture()
def byzantine_civilization():
    return Civilization(
        name='Byzantine',
    )


@pytest.fixture()
def english_army(english_civilization):
    return Army(
        civilization=english_civilization,
    )


@pytest.fixture()
def chinese_army(chinese_civilization):
    return Army(
        civilization=chinese_civilization,
    )


@pytest.fixture()
def byzantine_army(byzantine_civilization):
    return Army(
        civilization=byzantine_civilization,
    )
