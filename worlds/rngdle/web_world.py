from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class RNGdleWebWorld(WebWorld):
    game = "RNGdle"

    theme = "partyTime"

    setup_en = Tutorial(
        "setup"
        "setup guide"
        "English",
        "setup_en.md",
        "setup/en",
        ["TheMailmanGD"]
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets