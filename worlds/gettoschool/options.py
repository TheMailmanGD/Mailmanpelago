from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink

class deathlink(DeathLink):
    """
    Deathlink

    adds a test deathlink button
    """

    display_name = "Deathlink"

    default = False

@dataclass
class GodotAPOptions(PerGameCommonOptions):
    Deathlink: deathlink
    

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [DeathLink],
    ),
]

option_presets = {
    "default": {
        "Deathlink": False,
    },
}