from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import RNGdleWorld

ITEM_NAME_TO_ID = {
    "Progressive Roll Rarity" : 1,
    "Progressive Roll Rarity" : 2,
    "Progressive Roll Rarity" : 3,
    "Progressive Roll Rarity" : 4,
    "Progressive Roll Speed" : 5,
    "Progressive Roll Speed" : 6,
    "Progressive Roll Speed" : 7,
    "Swap To Best Neighbor" : 8,
    "Progressive Zero Chance" : 9,
    "Progressive Zero Chance" : 10,
    "Progressive Zero Chance" : 11,
    "Lock Number" : 12,
    "Swap To Worst Neighbor Trap" : 13,
    "Slow Rolls Trap" : 14,
    "6 Digit Lock Trap" : 15,
    "Bee Trap" : 16,
    "Luck" : 17
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Progressive Roll Rarity" : ItemClassification.progression,
    "Progressive Roll Speed" : ItemClassification.progression | ItemClassification.useful,
    "Swap To Best Neighbor" : ItemClassification.useful | ItemClassification.filler,
    "Progressive Zero Chance" : ItemClassification.progression | ItemClassification.useful,
    "Lock Number" : ItemClassification.useful,
    "Swap To Worst Neighbor Trap" : ItemClassification.trap,
    "Slow Rolls Trap" : ItemClassification.trap,
    "6 Digit Lock Trap" : ItemClassification.trap,
    "Bee Trap" : ItemClassification.trap,
    "Luck" : ItemClassification.filler
}

class RNGdleItem(Item):
    game = "RNGdle"

def get_random_filler_item_name(world: RNGdleWorld) -> str:
    a = world.random.randint(1, 100)
    if a > 60:
        if a > 90:
            return "Swap To Worst Neighbor Trap"
        elif a > 80:
            return "Slow Rolls Trap"
        elif a > 70:
            return "6 Digit Lock Trap"
        else:
            return "Bee Trap"
    else:
        if a > 30:
            return "Swap To Best Neighbor"
    return "Luck"

def create_item_with_correct_classification(world: RNGdleWorld, name: str) -> RNGdleItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return RNGdleItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: RNGdleWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Progressive Roll Rarity"),
        world.create_item("Progressive Roll Rarity"),
        world.create_item("Progressive Roll Rarity"),
        world.create_item("Progressive Roll Rarity"),
        world.create_item("Progressive Roll Speed"),
        world.create_item("Progressive Roll Speed"),
        world.create_item("Progressive Roll Speed"),
        world.create_item("Lock Number"),
        world.create_item("Progressive Zero Chance"),
        world.create_item("Progressive Zero Chance"),
        world.create_item("Progressive Zero Chance"),
    ]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    