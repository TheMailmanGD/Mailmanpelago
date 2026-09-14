from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink

class deathlink(DeathLink):
    """
    if you die, everyone dies. if anyone dies, you die.
    """

    display_name = "Deathlink"

@dataclass
class GodotAPOptions(PerGameCommonOptions):
    deathlink: deathlink

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [deathlink],
    ),
]

option_presets = {
    "default": {
        "deathlink": False,
    },
}