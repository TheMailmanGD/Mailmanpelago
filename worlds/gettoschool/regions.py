from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import gettoschoolworld

def create_and_connect_regions(world: gettoschoolworld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: gettoschoolworld) -> None:
    ending = Region("Ending", world.player, world.multiworld)
    choices = Region("Choices", world.player, world.multiworld)

    regions = [ending, choices]

    world.multiworld.regions += regions

def connect_regions(world: gettoschoolworld) -> None:
    ending = world.get_region("Ending")
    choices = world.get_region("Choices")

    choices_to_ending = Entrance(world.player, "Choices to Ending", parent=choices)
