# Pong Arcade Game

Welcome to **Pong Arcade Game**, a modern implementation of the classic two-player arcade game written in Python using the Turtle module. This project demonstrates object-oriented programming concepts, interactive gameplay, and user-friendly navigation with a menu system.

---

## Features

### Current Features:
- **Main Menu**:
  - Start the game, view instructions, or exit the application.
- **Two-player gameplay**:
  - Compete with another player using keyboard controls.
- **Dynamic ball physics**:
  - The ball bounces realistically off walls and paddles.
- **Score tracking and winning conditions**:
  - Displays scores for both players, with the game ending when one player reaches 5 points.
- **Instructions page**:
  - Learn the controls and game rules from the instructions screen.
- **Exit screen**:
  - A polished "Thanks for playing!" message before exiting the game.

### Planned Enhancements:
- **Enhanced Graphics**:
  - Add colorful paddles and a visually appealing ball design.
- **Sound Effects**:
  - Introduce sound effects for paddle hits, wall bounces, and scoring.
- **Customization**:
  - Allow players to choose paddle and ball colors.

---

## How to Play

1. **Start the Game**:
   - Run `main.py`.
   - Use the main menu to start the game by pressing `S`.
2. **Control the Paddles**:
   - **Player 1 (Right Paddle)**:
     - `Up Arrow`: Move up
     - `Down Arrow`: Move down
   - **Player 2 (Left Paddle)**:
     - `W`: Move up
     - `S`: Move down
3. **Gameplay**:
   - Prevent the ball from passing your paddle and try to score against your opponent.
   - The first player to reach 5 points wins.
4. **Other Controls**:
   - **Instructions**: Press `I` in the main menu to view controls and rules.
   - **Exit Game**: Press `E` from any screen to exit the game.

---

## Installation

### Prerequisites:
- Python 3.x must be installed on your system.

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pong-arcade-game.git
   ```
2. Navigate to the project folder:
   ```bash
   cd pong-arcade-game
   ```
3. Run the game:
   ```bash
   python main.py
   ```

---

## Project Structure

```
Pong Arcade Game/
│
├── main.py           # Main game logic and menu integration
├── menu.py           # Main menu and instructions screen
├── paddle.py         # Paddle behavior and controls
├── ball.py           # Ball behavior and movement
├── scoreboard.py     # Score tracking and game-over logic
└── README.md         # Project documentation
```

---

## Enhancements in Progress

### Enhanced Graphics
- **Goal**: Improve the visual appeal of the game.
  - Replace plain paddles and ball with colorful designs.
  - Add gradients or other decorations to the game elements.

### Sound Effects
- **Goal**: Make the game more immersive.
  - Add sound effects for paddle hits, wall bounces, and scoring events.

### Customization
- **Goal**: Provide options for personalization.
  - Allow players to select paddle colors and ball designs before starting the game.

---

## Contribution

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request describing your changes.

---

## Contact

For any questions or feedback, feel free to reach out:
- **Mail**: wlqinnovations@gmail.com
- **GitHub**: [wlqinnovations](https://github.com/wlqinnovations)