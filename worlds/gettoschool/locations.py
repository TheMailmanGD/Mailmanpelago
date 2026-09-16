from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification, Location

from .items import gettoschoolItem

if TYPE_CHECKING:
    from .world import gettoschoolworld

LOCATION_NAME_TO_ID = {
    "school" : 1,
    "sleepmania" : 2,
    "quitter" : 3,
}

class gettoschoolLocation(Location):
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
    ending.add_locations(ending_locations, location_type=gettoschoolLocation)

def create_events(world: gettoschoolworld) -> None:
    ending = world.get_region("Ending")
    ending.add_event(
        "All Endings Cleared", "Victory", location_type=gettoschoolLocation, item_type=gettoschoolItem
    )