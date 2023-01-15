import random


class Food:

    def __init__(self):
        self.location = None

    def relocate(self, world):
        locations = [(x, y) for x in range(world.width) for y in range(world.height)]
        for segment in world.snake.body:
            locations.remove(segment)
        self.location = random.choice(locations)