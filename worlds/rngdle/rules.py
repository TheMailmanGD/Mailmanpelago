from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import RNGdleWorld

def set_all_rules(world: RNGdleWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: RNGdleWorld) -> None:
    uncommon_to_rare = world.get_entrance("Uncommon to Rare")
    rare_to_epic = world.get_entrance("Rare to Epic")
    epic_to_anomaly = world.get_entrance("Epic to Anomaly")
    anomaly_to_mythic = world.get_entrance("Anomaly to Mythic")

    can_rare = HasAll("Progressive Roll Rarity")
    can_epic = HasAll("Progressive Roll Rarity", "Progressive Roll Rarity")
    can_anomaly = HasAll("Progressive Roll Rarity", "Progressive Roll Rarity", "Progressive Roll Rarity")
    can_mythic = HasAll("Progressive Roll Rarity", "Progressive Roll Rarity", "Progressive Roll Rarity", "Progressive Roll Rarity")

    world.set_rule(uncommon_to_rare, can_rare)
    world.set_rule(rare_to_epic, can_epic)
    world.set_rule(epic_to_anomaly, can_anomaly)
    world.set_rule(anomaly_to_mythic, can_mythic)

def set_all_location_rules(world: RNGdleWorld) -> None:
    can_rare: Rule = HasAll("Progressive Roll Rarity")
    can_epic: Rule = HasAll("Progressive Roll Rarity", "Progressive Roll Rarity")
    can_anomaly: Rule = HasAll("Progressive Roll Rarity", "Progressive Roll Rarity", "Progressive Roll Rarity")
    can_mythic: Rule = HasAll("Progressive Roll Rarity", "Progressive Roll Rarity", "Progressive Roll Rarity", "Progressive Roll Rarity")

    rare_locations = [
        "Three Quarter Century",
        "Semi Century",
        "Quarter Century",
        "Double Nine",
        "Century",
        "Mirror Bookends",
        "Bookends",
        "Three Pair",
        "Four Digits",
        "Paired Bookends",
        "Slopes",
        "Framed Double",
        "Metronome",
        "Steps",
        "Duality",
        "Scramble",
        "Divisible By Three",
        "Calendar",
        "E Slice (3)",
        "Pi Slice (3)",
        "Emergency",
        "Botanist",
        "Orientation",
        "Error 404",
        "Sequence (4)",
        "Devil",
        "Jackpot",
        "Contiguous Full House",
        "Heavy",
        "Secret Agent",
        "Turtle",
        "Deep Void(3)",
        "Contiguous Quads",
        "Palindrome",
        "2 Consecutive Numbers",
        "Firefly",
        "Even Spacing",
        "2nd Power",
        "10k EP",
        "20k EP",
    ]
    epic_locations = [
        "Colossal",
        "Semi-Millenium",
        "Triple Nine",
        "Pronic Number",
        "Millenium",
        "Echo",
        "Three Digits",
        "Decay",
        "Framed Quad",
        "Framed Triple",
        "Framed Pair",
        "Contiguous Three Pair",
        "3 Consecutive Numbers(Contains)",
        "Five Of A Kind",
        "Crescendo",
        "Ascension",
        "Zipper",
        "3 Consecutive Numbers(Scrambled)",
        "Tau Slice(4)",
        "E Slice(4)",
        "Pi Slice(4)",
        "Big Brother",
        "8008",
        "Hell",
        "Leet",
        "6767",
        "Deeper Meaning",
        "Very Nice",
        "Jackpot 4",
        "Straight",
        "Strobogrammatic",
        "Deep Void(4)",
        "Contiguous Fives",
        "Three Consecutive Numbers",
        "3rd Power",
        "30k EP",
    ]
    anomaly_locations = [
        "Semi-Epoch",
        "Quad Nine",
        "Epoch",
        "Spy Number",
        "Two Digits",
        "Straight Flush",
        "Binary Soul",
        "Funny Numbers",
        "Homogeneous",
        "4 Consecutive Numbers(Scrambled)",
        "4 Consecutive Numbers(Contains)",
        "Waterfall",
        "4th Power",
        "Fibonacci Number",
        "Cascade",
        "Tau Slice(5)",
        "E Slice(5)",
        "Pi Slice(5)",
        "80085",
        "58008",
        "Royal Flush",
        "Power Of Two",
        "Jackpot Five",
        "Fifth Power",
        "Power Of Three",
        "6th Power",
        "60k EP",
        "100k EP",
    ]
    mythic_locations = [
        "Semi-Eon",
        "Quint Nine",
        "Single Digit",
        "Deep Void(5)",
        "Contiguous Sixes",
        "Eon",
        "Sequence(6)",
        "Hello",
        "Factorial",
        "Power Of Five",
        "Power Of Seven",
        "7th Power",
        "Ouroboros",
        "8th Power",
        "9th Power",
        "4 Consecutive Numbers",
        "Euler's Number",
        "Pi",
        "11th Power",
        "10th Power",
        "Golden Ratio",
        "Tau",
        "19th Power",
        "17th Power",
        "13th Power",
        "Always",
        "Funny Number",
        "Exact Boob",
        "One Million",
        "Full Day",
        "Groundhog Day",
        "Brainrot",
        "Exact Calendar",
        "Exact Orientation",
        "Exact Eighty-Six",
        "Exact Six-Seven",
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two",
        "One",
        "Zero",
        "Orwellian",
        "Universal Answer",
        "Mayday",
        "Hotbox",
        "Very Very Nice",
        "17776",
        "Infernal",
        "Not Found",
        "Exact Emergency",
        "Exact Meaning",
        "Exact 80085",
        "Exact Hell",
        "Exact Leet",
        "Exact Devil",
        "Exact Botanist",
        "Jackpot Six",
        "Exact Jackpot",
        "Exact Nice",
        "1M EP",
        "100M EP",
    ]
    for location_name in rare_locations:
        world.set_rule(world.get_location(location_name), can_rare)

    for location_name in epic_locations:
        world.set_rule(world.get_location(location_name), can_epic)

    for location_name in anomaly_locations:
        world.set_rule(world.get_location(location_name), can_anomaly)

    for location_name in mythic_locations:
        world.set_rule(world.get_location(location_name), can_mythic)

def set_completion_condition(world: RNGdleWorld) -> None:
    world.set_completion_rule(HasAll(
        "Progressive Roll Rarity",
        "Progressive Roll Rarity",
        "Progressive Roll Rarity",
        "Progressive Roll Rarity",
        "Progressive Zero Chance",
        "Progressive Zero Chance",
        "Progressive Zero Chance",
        "Progressive Roll Speed",
        "Progressive Roll Speed",
        "Progressive Roll Speed"
    ))