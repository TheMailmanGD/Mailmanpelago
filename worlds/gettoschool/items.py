from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import gettoschoolworld

ITEM_NAME_TO_ID = {
    "Option1" : 1,
    "Option2" : 2,
    "Option3" : 3,
    "Option4" : 4,
    "beef" : 5,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Option1" : ItemClassification.progression,
    "Option2" : ItemClassification.progression,
    "Option3" : ItemClassification.useful,
    "Option4" : ItemClassification.progression,
    "beef" : ItemClassification.filler,
}

class gettoschoolItem(Item):
    game = "Get to School"

def get_random_filler_item_name(world: gettoschoolworld) -> str:
    return "beef"

def create_item_with_correct_classification(world: gettoschoolworld, name: str) -> gettoschoolItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS.get(name, ItemClassification.filler)
    return gettoschoolItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: gettoschoolworld) -> None:
    itempool: list[Item] = [
        world.create_item("Option1"),
        world.create_item("Option2"),
        world.create_item("Option3"),
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool

    starting_option4 = world.create_item("Option4")
    world.push_precollected(starting_option4)