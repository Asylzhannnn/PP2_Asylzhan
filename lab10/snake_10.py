import pygame
import random
import sys
import psycopg2

# Настройки экрана и блока
block_size = 25
screen_width = 700
screen_height = 700
cols = screen_width // block_size
rows = screen_height // block_size

# Подключение к базе
def create_database_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="lab10",
        user="postgres",
        password="Asylzhan2007",
        port="5432"
    )

# Получаем пользователя
def get_user(username):
    conn = create_database_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "User" WHERE username = %s', (username,))
    user = cur.fetchone()
    conn.close()
    return user

# Создаем пользователя
def create_user(username):
    conn = create_database_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO "User" (username, current_level, current_score) VALUES (%s, %s, %s)',
                (username, 0, 0))
    conn.commit()
    conn.close()

# Обновляем пользователя
def update_user(username, score, level):
    conn = create_database_connection()
    cur = conn.cursor()
    cur.execute('UPDATE "User" SET current_score = %s, current_level = %s WHERE username = %s',
                (score, level, username))
    conn.commit()
    conn.close()

# Точка
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Змейка
class Snake:
    def __init__(self):
        self.body = [Point(5, 5)]
        self.direction = (0, 0)

    def move(self):
        head = self.body[0]
        dx, dy = self.direction
        new_head = Point(head.x + dx, head.y + dy)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(Point(self.body[-1].x, self.body[-1].y))

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, 'green',
                             pygame.Rect(segment.x * block_size, segment.y * block_size,
                                         block_size, block_size))

    def get_head(self):
        return self.body[0]

    def check_collision_with_self(self):
        return self.get_head() in self.body[1:]

# Еда
class Food:
    def __init__(self):
        self.relocate()

    def relocate(self):
        self.x = random.randint(0, cols - 1)
        self.y = random.randint(0, rows - 1)

    def draw(self, screen):
        pygame.draw.rect(screen, 'red',
                         pygame.Rect(self.x * block_size, self.y * block_size,
                                     block_size, block_size))

# Уровни
def get_walls(level):
    walls = []
    if level == 1:
        for x in range(0, cols):
            if x != cols // 2:  # проход
                walls.append(Point(x, rows // 2))
    elif level == 2:
        for y in range(0, rows):
            if y != rows // 3:
                walls.append(Point(cols // 3, y))
            if y != 2 * rows // 3:
                walls.append(Point(2 * cols // 3, y))
    return walls

def draw_walls(screen, walls):
    for wall in walls:
        pygame.draw.rect(screen, 'blue',
                         pygame.Rect(wall.x * block_size, wall.y * block_size,
                                     block_size, block_size))

def wall_collision(head, walls):
    return any(head.x == wall.x and head.y == wall.y for wall in walls)

# Сетка
def draw_grid(screen):
    for x in range(0, screen_width, block_size):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, screen_height))
    for y in range(0, screen_height, block_size):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (screen_width, y))

# Главная игра
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 25)

    username = input("Enter username: ")
    user = get_user(username)
    if not user:
        create_user(username)
        user = get_user(username)

    score = user[3]
    level = user[2]

    snake = Snake()
    food = Food()
    walls = get_walls(level)
    pause = False

    dx, dy = 0, 0
    snake.direction = (dx, dy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_user(username, score, level)
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)
                elif event.key == pygame.K_p:
                    pause = True
                    update_user(username, score, level)
                elif event.key == pygame.K_u:
                    pause = False

        if pause:
            continue

        screen.fill('black')
        draw_grid(screen)

        snake.move()
        head = snake.get_head()

        if head.x == food.x and head.y == food.y:
            snake.grow()
            food.relocate()
            score += 1
            if score % 5 == 0:
                level += 1
                walls = get_walls(level)

        if (head.x < 0 or head.x >= cols or head.y < 0 or head.y >= rows or
                snake.check_collision_with_self() or wall_collision(head, walls)):
            print("Game over")
            update_user(username, score, level)
            pygame.quit()
            sys.exit()

        snake.draw(screen)
        food.draw(screen)
        draw_walls(screen, walls)

        screen.blit(font.render(f"Score: {score}", True, 'white'), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, 'white'), (10, 40))

        pygame.display.flip()
        clock.tick(8 + level)

if __name__ == "__main__":
    main()