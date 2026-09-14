from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import gettoschoolworld

LOCATION_NAME_TO_ID = {
    "school" : 1,
    "sleepmania" : 2,
    "quitter" : 3,
}

class gettoschoolLocation():
    game = "Get to School"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: gettoschoolworld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: gettoschoolworld) -> None:
    ending = world.get_region("Ending")
    choices = world.get_region("Choices")

    ending_locations = get_location_names_with_ids(
        ["school", "sleepmania", "quitter"]
    )
    ending.add_locations(ending_locations)

def create_events(world: gettoschoolworld) -> None:
    pass
    # ending = world.get_region("Ending")
    # ending.add_event(
    #     "all_endings", "Victory", location_type=gettoschoolLocation, item_type=items.gettoschoolItem
    #     )