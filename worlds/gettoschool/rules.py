from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import gettoschoolworld

def set_all_rules(world: gettoschoolworld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: gettoschoolworld) -> None:
    choices_to_ending = world.get_entrance("Choices to Ending")

    can_get_sleepmania = HasAll("Option1", "Option2")
    world.set_rule(choices_to_ending, can_get_sleepmania)
    can_get_quitter = Has("Option4")
    world.set_rule(choices_to_ending, can_get_quitter)
    can_get_school = HasAll("Option1", "Option4")
    world.set_rule(choices_to_ending, can_get_school)

def set_all_location_rules(world: gettoschoolworld) -> None:
    choices_to_ending = world.get_entrance("Choices to Ending")
    can_get_sleepmania = HasAll("Option1", "Option2")
    world.set_rule(choices_to_ending, can_get_sleepmania)
    can_get_quitter = Has("Option4")
    world.set_rule(choices_to_ending, can_get_quitter)
    can_get_school = HasAll("Option1", "Option4")
    world.set_rule(choices_to_ending, can_get_school)

def set_completion_condition(world: gettoschoolworld) -> None:
    world.set_completion_rule(HasAll("Option1", "Option2", "Option4"))