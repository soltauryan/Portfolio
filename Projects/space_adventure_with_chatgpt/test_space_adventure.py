import unittest
from unittest.mock import patch, MagicMock
from space_adventure import Player, ShipStatus, Universe, EventSystem, ChatInterface, SHIP_TYPES

class TestSpaceAdventure(unittest.TestCase):

    def setUp(self):
        self.player = Player("Test Player")
        self.ship = ShipStatus("Test Ship", SHIP_TYPES["Corvette"])
        self.universe = Universe("Test System")
        self.event_system = EventSystem()
        self.chat = ChatInterface("Test Player", "Test Ship", "Test Description")

    @patch('space_adventure.client.chat.completions.create')
    def test_event_generation(self, mock_openai):
        # Simulate OpenAI API response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = """Event: Mysterious Nebula
Description: Your ship encounters a colorful, swirling nebula that seems to emit strange energy readings.
Impact: The nebula's radiation temporarily boosts your ship's sensor capabilities."""
        mock_openai.return_value = mock_response

        event_info = self.event_system.generate_event("cosmic_phenomenon", self.player, self.ship, self.universe)
        
        self.assertIn("Mysterious Nebula", event_info)
        self.assertIn("colorful, swirling nebula", event_info)
        self.assertIn("boosts your ship's sensor capabilities", event_info)

    @patch('space_adventure.client.chat.completions.create')
    def test_chat_interface(self, mock_openai):
        # Simulate OpenAI API response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Greetings, captain! Your ship's systems are fully operational. What would you like to do?"
        mock_openai.return_value = mock_response

        response = self.chat.send_message("Check ship status", self.ship.get_status_report(), "No nearby ships")
        
        self.assertIn("Greetings, captain!", response)
        self.assertIn("systems are fully operational", response)

    def test_ship_damage_and_repair(self):
        initial_hull = self.ship.hull
        self.ship.damage_system("hull", 20)
        self.assertEqual(self.ship.hull, initial_hull - 20)

        self.ship.repair_system("hull", 10)
        self.assertEqual(self.ship.hull, initial_hull - 10)

    def test_player_experience_gain(self):
        initial_exp = self.player.experience
        self.player.gain_experience(100)
        self.assertEqual(self.player.experience, initial_exp + 100)

    def test_universe_travel(self):
        initial_location = self.universe.current_location
        self.universe.travel_to("New System")
        self.assertEqual(self.universe.current_location, "New System")
        self.assertIn("New System", self.universe.discovered_locations)

if __name__ == '__main__':
    unittest.main()