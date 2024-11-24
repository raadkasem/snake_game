# Snake Game

A simple snake game implemented using Python and Pygame. The game allows you to control the snake using arrow keys, and the objective is to eat food without colliding with the walls or itself.

## Project Structure

```
snake_game/
│
├── assets/
│   └── beepsound.wav
│
├── snake_game.py
└── README.md
```

## Features

- **Object-Oriented Design:** The game is structured using classes, making it modular and easy to maintain.
- **Sound Effects:** Beep sounds are played when the snake eats food or collides (loses).
- **User Interface:** Basic UI elements are implemented using Pygame.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/snake_game.git
   cd snake_game
   ```

2. Install dependencies:

   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python snake_game.py
   ```

## Controls

- **Arrow Keys:** Move the snake in the desired direction.
- **Q Key:** Quit the game.
- **C Key:** Restart the game after losing.

## Contact

Developer: Raad Kasem  
Email: ra3dkasem@gmail.com

## License

This project is licensed under the MIT License.

### UI Enhancements

- **Sound Effects:** Added beep sounds for eating food and collisions.
- **Game Over Message:** Improved the game over message with clearer instructions.

### Additional Notes

Make sure you have a `beepsound.wav` file in the `assets/` directory for the sound effects to work. You can add any beep sound you like.
