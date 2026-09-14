from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class gtsWeb(WebWorld):
    game = "Get to School"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Get to School for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["themailmangd", "anonymous"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets