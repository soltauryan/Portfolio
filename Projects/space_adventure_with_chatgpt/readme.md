# Space Adventure with ChatGPT

## Overview

"Space Adventure with ChatGPT" is an interactive text-based game where players embark on a space journey, making decisions and encountering various events. The game leverages OpenAI's GPT-4o-mini model to generate dynamic and engaging events based on the player's actions and the current state of the game.

## Features

- **Player and Ship Management**: Create and manage a player character and their ship, including attributes like experience, skills, and ship systems.
- **Dynamic Events**: Generate random events that impact the player's journey, such as alien encounters, cosmic phenomena, and technological discoveries.
- **Interactive Chat Interface**: Communicate with the ship's AI to navigate the universe, make decisions, and respond to events.
- **Universe Exploration**: Travel through different galaxies, each with its own characteristics and potential encounters.
- **Custom Scenarios**: Choose from predefined starting scenarios or create a custom scenario to begin your adventure.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/space_adventure_with_chatgpt.git
   cd space_adventure_with_chatgpt
   ```
2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```
3. **Set up OpenAI API Key**:

   - Obtain an API key from OpenAI.
   - Set the `OPENAI_API_KEY` environment variable:
     ```sh
     export OPENAI_API_KEY='your_openai_api_key'
     ```

## Usage

1. **Run the game**:

   ```sh
   python space_adventure.py
   ```
2. **Follow the on-screen instructions** to create your player, choose a starting scenario, and begin your space adventure.

## How to Play

- **Commands**: Type your actions or dialogue as if you're interacting with your ship's AI. Some common commands include:
  - `Scan [area/object]`
  - `Navigate to [coordinates/celestial body]`
  - `Analyze [anomaly/signal]`
  - `Use [ship system/equipment]`
  - `Communicate with [alien life/other ships]`
- **Help**: Type `help` at any time to see the instructions again.
- **Quit**: Type `quit` to end the mission.

## Project Structure

- `space_adventure.py`: Main game script containing all the classes and logic for the game.
- `requirements.txt`: List of dependencies required to run the game.

## Key Classes and Functions

- **Player**: Manages player attributes like name, experience, and skills.
- **ShipType**: Defines different types of ships with their attributes.
- **ShipStatus**: Manages the status of the player's ship, including systems, cargo, and fuel.
- **Galaxy**: Represents a galaxy with its name and controlling faction.
- **Universe**: Manages the current state of the universe, including galaxies, locations, and nearby ships.
- **EventSystem**: Generates and manages random events that occur during the game.
- **ChatInterface**: Handles communication between the player and the ship's AI.
- **print_instructions()**: Prints the game instructions.
- **choose_starting_scenario()**: Allows the player to choose a starting scenario.
- **main()**: Main function to start the game.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact: soltauryan@gmail.com



Enjoy your space adventure!
