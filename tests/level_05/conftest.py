import pytest

from dungeon.hero import Hero
from dungeon.inventory import Inventory, Item
from dungeon.shop import Listing, Shop


@pytest.fixture
def hero():
    return Hero("Ada")

@pytest.fixture
def rich_hero(hero):
    hero.gold = 100
    return hero

@pytest.fixture
def backpack():
    return Inventory()

@pytest.fixture
def potion():
    return Item("potion", weight=0.5, value=11)

@pytest.fixture
def shop(potion):
    return Shop([Listing(potion, price=8, stock=3)])
