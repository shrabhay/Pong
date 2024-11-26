# Pong Game
## Description
A simple implementation of the classic arcade game "Pong" using Python's `turtle` graphics module. This project consists of several Python files that define the key components of the game, including the ball, paddles, scoreboard, and the main game logic.

---

## Files Overview

1. **`ball.py`**: Contains the `Ball` class, which controls all ball-related functionality (movement, bouncing off walls and paddles, and resetting the ball's position).
2. **`paddle.py`**: Contains the `Paddle` class, which defines the paddles for both players and controls their movement (up and down).
3. **`scoreboard.py`**: Contains the `Scoreboard` class, responsible for displaying and updating the score for both players.
4. **`the_pong_game.py`**: The main file that sets up the game, including initializing the screen, paddles, ball, and scoreboards. It also handles user inputs and the game loop.

---

## How to Run

1. Ensure that you have Python installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
   
2. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/shrabhay/Pong.git
   cd pong-game
   ```

3. Install the `turtle` module if it's not already installed. It is typically pre-installed with Python, but if needed, you can install it via pip (for non-Windows systems):
    ```bash
    pip3 install PythonTurtle
    ```

4. Run the game by executing the `the_pong_game.py` file:
    ```bash
    python3 the_pong_game.py
    ```

---

## Game Controls
* Player 1 (Left Paddle):
  * Move Up: W key
  * Move Down: S key
* Player 2 (Right Paddle):
  * Move Up: Up Arrow key
  * Move Down: Down Arrow key

---

## Features
* *Two-player mode*: Players control paddles on the left and right sides.
* *Score tracking*: The score is displayed at the top, with each player getting a point when the ball passes the opponent's paddle.
* *Ball bouncing*: The ball bounces off the top and bottom walls, as well as the paddles.
* *Ball reset*: When the ball passes a paddle, it resets to the center and continues with the game.
* *Speed increase*: The ball speed gradually increases after each paddle bounce.

---

## License
This project is open-source and available under the MIT License.

---

## Credits
This game was built using Python's turtle graphics module. The game logic and design were created as part of a simple Pong game implementation.
