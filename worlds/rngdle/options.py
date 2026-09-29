from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink

class DeathLink(DeathLink):
    """
    Enables deathlink.
    In deathlink, rolling a trash roll kills other players with the option enabled.
    Rolling a certain amount of common rolls also can do this.
    """
    display_name = "Death Link"

class DeathLinkAmnesty(Range):
    """
    How many common rolls it takes to send a DeathLink
    """
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 50
    default = 10

class TrapExpirationAmount(Range):
    """
    The amount of rolls it takes for a trap to expire
    """
    display_name = "Trap Expiration Amount"
    range_start = 1
    range_end = 50
    default = 5

@dataclass
class RNGdleOptions(PerGameCommonOptions):
    deathlink: DeathLink
    deathlinkamnesty: DeathLinkAmnesty
    trapexpirationamount: TrapExpirationAmount

option_groups = {
    OptionGroup(
        "DeathLink"
        [DeathLink, DeathLinkAmnesty]
    ),
    OptionGroup(
        "Traps"
        [TrapExpirationAmount]
    )
}

option_presets = {
    "default": {
        "deathlink" : False,
        "deathlinkamnesty" : 10,
        "trapexpirationamount" : 5,
    }
}