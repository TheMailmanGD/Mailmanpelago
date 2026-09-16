from test.bases import WorldTestBase

from worlds.gettoschool.world import gettoschoolworld


class GetToSchoolTestBase(WorldTestBase):
    game = "Get to School"
    world: gettoschoolworld


class TestGetToSchoolWinCondition(GetToSchoolTestBase):
    def test_victory_event_exists(self) -> None:
        ending_locations = {location.name for location in self.world.get_region("Ending").locations}

        self.assertIn("school", ending_locations)
        self.assertIn("sleepmania", ending_locations)
        self.assertIn("quitter", ending_locations)
        self.assertIn("All Endings Cleared", ending_locations)

        victory_event = next(
            location for location in self.world.get_region("Ending").locations
            if location.name == "All Endings Cleared"
        )
        self.assertEqual(victory_event.item.name, "Victory")
