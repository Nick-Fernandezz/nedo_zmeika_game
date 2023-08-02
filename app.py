import pygame
from random import randint


class Point():
    def __init__(self) -> None:
        self.x = randint(0, Game.display.get_width())
        self.y = randint(0, Game.display.get_height())
        self.color = (randint(1, 255), randint(1, 255), randint(1, 255))
        self.point = pygame.Surface((20, 20))
        self.point.fill(self.color)



class Snake():

    DIRECTION_RIGHT = 0
    DIRECTION_DOWN = 1
    DIRECTION_LEFT = 2
    DIRECTION_UP = 4

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.direction = 0
        self.color = (41, 145, 60)
        self.snake = pygame.Surface((40, 40))
        self.snake.fill((41, 145, 60))
        self.speed = 1
    

    def move(self) -> None:
        if self.direction == self.DIRECTION_LEFT and self.direction != self.DIRECTION_RIGHT:
            self.x -= self.speed
        elif self.direction == self.DIRECTION_DOWN and self.direction != self.DIRECTION_UP:
            self.y += self.speed
        elif self.direction == self.DIRECTION_RIGHT and self.direction != self.DIRECTION_LEFT:
            self.x += self.speed
        elif self.direction == self.DIRECTION_UP and self.direction != self.DIRECTION_DOWN:
            self.y -= self.speed

        if self.x < 0:
            self.x = Game.display.get_width()
        elif self.x > Game.display.get_width():
            self.x = 0
        elif self.y < 0:
            self.y = Game.display.get_height()
        elif self.y > Game.display.get_height():
            self.y = 0

class Game():
    pygame.init()
    display = pygame.display.set_mode((1000, 700))
    font = pygame.font.Font("fonts/Montserrat-VariableFont_wght.ttf", 40)


    def __init__(self) -> None:
        self.xp = 0
        pygame.display.set_caption("Snake")
        self.start_game()
    

    def start_game(self):
        running = True
        snake = Snake()
        points = []
        while running:
            pygame.display.update()
            self.display.fill('black')
            self.display.blit(snake.snake, (snake.x, snake.y))
            self.display.blit(
                self.font.render(f"XP: {self.xp}", True, 'white'),
                (40, 40)
            )
            snake.move()
            keys = pygame.key.get_pressed()

            if len(points) < 3:
                points.append(Point())
            for point in points:
                self.display.blit(point.point, (point.x, point.y))
                if (snake.x <= point.x <= snake.x + snake.snake.get_width() and 
                    snake.y + snake.snake.get_height() >=  point.y >= snake.y):
                    self.xp += 10
                    del points[points.index(point)]
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                snake.direction = snake.DIRECTION_LEFT
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                snake.direction = snake.DIRECTION_DOWN
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                snake.direction = snake.DIRECTION_RIGHT
            elif keys[pygame.K_w] or keys[pygame.K_UP]:
                snake.direction = snake.DIRECTION_UP

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

if __name__ == "__main__":
    game = Game()
