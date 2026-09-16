from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class test(Toggle):
    """
    test
    """

    display_name = "Test Option"

    default = False

@dataclass
class GodotAPOptions(PerGameCommonOptions):
    test: test
    

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [test],
    ),
]

option_presets = {
    "default": {
        "test": False,
    },
}