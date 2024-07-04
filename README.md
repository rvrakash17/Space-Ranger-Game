# Space Ranger Game

A simple space-themed game built with Pygame where players control a spaceship to avoid falling meteors. The goal is to achieve the highest score by surviving as long as possible and dodging meteors that increase in speed over time.

## Features

- **Space Background:** Dynamic background image for the game environment.
- **Spaceship Control:** Move the spaceship left and right using keyboard controls.
- **Meteor Dodging:** Avoid falling meteors that increase in speed as the game progresses.
- **Score Tracking:** Displays the current score based on the number of meteors avoided.
- **Game Over Screen:** Shows a game over message when the spaceship collides with a meteor.

## Technologies Used

- **Python:** Programming language used for the game logic.
- **Pygame:** Library for creating games and multimedia applications.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/rvrakash17/Space-Ranger-Game.git
   cd Space-Ranger-Game
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then install Pygame using pip:
   ```sh
   pip install pygame
   ```

3. **Download Assets:**
   Ensure you have the following image files in your project directory:
   - `Space BG.png` (Background image)
   - `Gametitle.png` (Title image)
   - `Start Msg.png` (Start message image)
   - `Spaceship.png` (Spaceship image)
   - `Meteor.png` (Meteor image)
   - `Game Over.png` (Game over image)

## Usage

1. **Run the Game:**
   Execute the game script:
   ```sh
   python spacegame.py
   ```

2. **Controls:**
   - **Start Game:** Press the `S` key to start the game.
   - **Move Left:** Press the `A` key or the left arrow key.
   - **Move Right:** Press the `D` key or the right arrow key.
   - **Restart Game:** Press the `R` key to restart the game after a game over.

3. **Objective:**
   - Avoid meteors falling from the top of the screen.
   - Increase your score by dodging meteors.
   - Survive as long as possible to achieve a high score.

## Code Explanation

### Initialization

- **Setup:** Initializes Pygame, sets up the display window, and loads images for various game elements.
- **Variables:** Defines game variables such as speed, score, and positions of game objects.

### Game Loop

- **Event Handling:** Handles user inputs (e.g., key presses) and game events (e.g., collision detection).
- **Movement:** Updates the position of the spaceship and meteors.
- **Collision Detection:** Checks if the spaceship collides with a meteor and displays the game over screen if so.
- **Score Update:** Increases the score and adjusts meteor speed as the player progresses.

### Rendering

- **Drawing:** Renders the background, spaceship, meteors, and score on the screen.
- **Game Over:** Displays a game over screen when the game ends.

## Author

- **Akash R**
