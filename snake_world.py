import pygame

from snake import Snake
from food import Food


class SnakeWorld:

    def __init__(self):
        self.tile_size = 20
        self.width = 20
        self.height = 15
        self.left = 0
        self.top = 0

        self.snake = Snake()
        self.foods = [Food()]
        self.score = 0

        for food in self.foods:
            food.relocate(world=self)

        self.font = pygame.font.SysFont("comicsans", 32)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            new_direction = (1, 0)
        elif keys[pygame.K_UP]:
            new_direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            new_direction = (0, 1)
        else:
            new_direction = self.snake.direction

        self.snake.change_direction(new_direction=new_direction)
        self.snake.update(world=self)
        for food in self.foods:
            if self.snake.head == food.location:
                self.snake.grow()
                food.relocate(world=self)
                self.score += 1

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.left * self.tile_size, self.top * self.tile_size, self.width * self.tile_size, self.height * self.tile_size))

        for food in self.foods:
            if not food.location:
                continue
            rect = (food.location[0] * self.tile_size, food.location[1] * self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(window, (0, 255, 0), rect)

        for segment in self.snake.body:
            rect = (segment[0] * self.tile_size, segment[1] * self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(window, (255, 0, 0), rect)

        dashboard_rect = (self.left, self.height * self.tile_size, self.width * self.tile_size, 40)
        pygame.draw.rect(window, (150, 150, 150), dashboard_rect)

        score = self.font.render(str(self.score), True, (0, 0, 255))
        score_position = ((self.width - 3) * self.tile_size, self.height * self.tile_size - 4)
        window.blit(score, score_position)

        if not self.snake.alive:
            game_over = self.font.render(str("Game Over"), True, (0, 0, 0))
            game_over_position = (3 * self.tile_size, self.height * self.tile_size - 4)
            window.blit(game_over, game_over_position)