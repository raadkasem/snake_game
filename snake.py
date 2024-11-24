import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Display settings
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
DISPLAY_WIDTH = CELL_SIZE * GRID_WIDTH
DISPLAY_HEIGHT = CELL_SIZE * GRID_HEIGHT

# Create the display
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set the clock
clock = pygame.time.Clock()

# Font for messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load beep sound
beep_sound = pygame.mixer.Sound("assets/beepsound.wav")


class Snake:
    def __init__(self):
        self.body = [(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[-1]

        if self.direction == "UP":
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + CELL_SIZE)
        elif self.direction == "LEFT":
            new_head = (head_x - CELL_SIZE, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + CELL_SIZE, head_y)

        self.body.append(new_head)
        self.body.pop(0)

    def turn(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(
                game_display, GREEN, [segment[0], segment[1], CELL_SIZE, CELL_SIZE]
            )

    def check_collision(self):
        head_x, head_y = self.body[-1]

        # Check walls
        if (
            head_x < 0
            or head_x >= DISPLAY_WIDTH
            or head_y < 0
            or head_y >= DISPLAY_HEIGHT
        ):
            return True

        # Check self-collision
        if self.body[-1] in self.body[:-1]:
            return True

        return False


class Food:
    def __init__(self, snake):
        self.snake = snake
        self.position = self.generate_position()

    def generate_position(self):
        while True:
            x = round(random.randrange(0, DISPLAY_WIDTH) / CELL_SIZE) * CELL_SIZE
            y = round(random.randrange(0, DISPLAY_HEIGHT) / CELL_SIZE) * CELL_SIZE
            if (x, y) not in self.snake.body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(
            game_display,
            RED,
            [self.position[0], self.position[1], CELL_SIZE, CELL_SIZE],
        )


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [DISPLAY_WIDTH / 6, DISPLAY_HEIGHT / 3])


def gameLoop():
    game_over = False
    game_close = False

    snake = Snake()
    food = Food(snake)

    while not game_over:

        while game_close == True:
            game_display.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.turn("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.turn("RIGHT")
                elif event.key == pygame.K_UP:
                    snake.turn("UP")
                elif event.key == pygame.K_DOWN:
                    snake.turn("DOWN")

        if snake.check_collision():
            beep_sound.play()
            game_close = True

        snake.move()

        if snake.body[-1] == food.position:
            beep_sound.play()
            food = Food(snake)

        game_display.fill(BLACK)
        snake.draw()
        food.draw()
        pygame.display.update()

        clock.tick(10)

    pygame.quit()
    quit()


if __name__ == "__main__":
    gameLoop()
