from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import RNGdleWorld

def create_and_connect_regions(world: APQuestWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: RNGdleWorld) -> None:
    uncommon = Region("Uncommon", world.player, world.multiworld)
    rare = Region("Rare", world.player, world.multiworld)
    epic = Region("Epic", world.player, world.multiworld)
    anomaly = Region("Anomaly", world.player, world.multiworld)
    mythic = Region("Mythic", world.player, world.multiworld)

    regions = [uncommon, rare, epic, anomaly, mythic]

    world.multiworld.regions += regions

def connect_regions(world: RNGdleWorld) -> None:
    uncommon = world.get_region("Uncommon")
    rare = world.get_region("Rare")
    epic = world.get_region("Epic")
    anomaly = world.get_region("Anomaly")
    mythic = world.get_region("Mythic")

    uncommon.connect(rare, "Uncommon to Rare")
    rare.connect(epic, "Rare to Epic")
    epic.connect(anomaly, "Epic to Anomaly")
    anomaly.connect(mythic, "Anomaly to Mythic")