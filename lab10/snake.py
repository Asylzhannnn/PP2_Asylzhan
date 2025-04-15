import pygame
import random
import sys
import psycopg2
from psycopg2 import OperationalError
from datetime import datetime

# Настройки игры
BLOCK_SIZE = 25
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
FPS = 60

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Настройки базы данных
DB_CONFIG = {
    "host": "localhost",
    "dbname": "lab10",
    "user": "postgres",
    "password": "Asylzhan2007",
    "port": "5432"
}

class Database:
    def __init__(self):
        self.conn = None
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            return True
        except OperationalError as e:
            print(f"Error in connecting to database: {e}")
            return False
    
    def create_tables(self):
        try:
            cur = self.conn.cursor()
            
            # Таблица пользователей
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            
            # Таблица результатов
            cur.execute("""
                CREATE TABLE IF NOT EXISTS scores (
                    score_id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(user_id),
                    score INTEGER NOT NULL,
                    level INTEGER NOT NULL,
                    game_time INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error in creating tables: {e}")
            return False
    
    def get_user(self, username):
        try:
            cur = self.conn.cursor()
            cur.execute('SELECT user_id FROM users WHERE username = %s', (username,))
            return cur.fetchone()
        except psycopg2.Error as e:
            print(f"Error when you get user: {e}")
            return None
    
    def create_user(self, username):
        try:
            cur = self.conn.cursor()
            cur.execute(
                'INSERT INTO users (username) VALUES (%s) RETURNING user_id', 
                (username,)
            )
            user_id = cur.fetchone()[0]
            self.conn.commit()
            return user_id
        except psycopg2.Error as e:
            print(f"Error in creating user: {e}")
            return None
    
    def save_score(self, user_id, score, level, game_time):
        try:
            cur = self.conn.cursor()
            cur.execute(
                'INSERT INTO scores (user_id, score, level, game_time) VALUES (%s, %s, %s, %s)',
                (user_id, score, level, game_time)
            )
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error in creating result: {e}")
            return False
    
    def get_user_scores(self, user_id, limit=5):
        try:
            cur = self.conn.cursor()
            cur.execute(
                'SELECT score, level, game_time FROM scores WHERE user_id = %s ORDER BY score DESC LIMIT %s',
                (user_id, limit)
            )
            return cur.fetchall()
        except psycopg2.Error as e:
            print(f"Error in getting results: {e}")
            return []
    
    def close(self):
        if self.conn:
            self.conn.close()

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.body = [
            [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2],
            [SCREEN_WIDTH // 2 - BLOCK_SIZE, SCREEN_HEIGHT // 2],
            [SCREEN_WIDTH // 2 - 2 * BLOCK_SIZE, SCREEN_HEIGHT // 2]
        ]
        self.direction = [1, 0]  #Начальное направление: вправо
        self.grow = False
    
    def move(self):
        head = [self.body[0][0] + self.direction[0] * BLOCK_SIZE, 
                self.body[0][1] + self.direction[1] * BLOCK_SIZE]
        self.body.insert(0, head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, dx, dy):
        #Запрещаем движение в противоположном направлении
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = [dx, dy]
    
    def check_collision(self, walls=None):
        head = self.body[0]
        
        #Проверка столкновения с границами экрана
        if (head[0] < 0 or head[0] >= SCREEN_WIDTH or 
            head[1] < 0 or head[1] >= SCREEN_HEIGHT):
            return True
        
        #Проверка столкновения с собой
        for segment in self.body[1:]:
            if head == segment:
                return True
        
        #Проверка столкновения со стенами (если есть)
        if walls:
            for wall in walls:
                if (head[0] >= wall[0] and head[0] < wall[0] + wall[2] and
                    head[1] >= wall[1] and head[1] < wall[1] + wall[3]):
                    return True
        
        return False
    
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(
                surface, GREEN,
                pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE)
            )

class Food:
    def __init__(self):
        self.pos = [0, 0]
        self.weight = 1
        self.spawn_time = pygame.time.get_ticks()
        self.randomize()
    
    def randomize(self, snake_body=None):
        while True:
            self.pos = [
                random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            ]
            self.weight = random.choice([1, 2, 3])
            self.spawn_time = pygame.time.get_ticks()
            
            # Проверяем, чтобы еда не появилась на змейке
            if snake_body is None or self.pos not in snake_body:
                break
    
    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 10000  # 10 секунд
    
    def draw(self, surface):
        color = RED if self.weight == 1 else BLUE if self.weight == 2 else (255, 165, 0)
        pygame.draw.rect(
            surface, color,
            pygame.Rect(self.pos[0], self.pos[1], BLOCK_SIZE, BLOCK_SIZE)
        )

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def show_game_over(surface, score, level, game_time):
    surface.fill(BLACK)
    
    draw_text(surface, "GAME OVER", 64, 
              SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100, RED)
    
    draw_text(surface, f"Final Score: {score}", 36, 
              SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, WHITE)
    
    draw_text(surface, f"Level: {level}", 36, 
              SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, WHITE)
    
    draw_text(surface, f"Time: {game_time // 1000} sec", 36, 
              SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, WHITE)
    
    draw_text(surface, "Press SPACE to restart or ESC to quit", 24, 
              SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 180, WHITE)
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "restart"
                elif event.key == pygame.K_ESCAPE:
                    return "quit"

def main():
    # Инициализация базы данных
    db = Database()
    if not db.connect():
        print("Cant connect to database.Game starts without saving.")
    
    if db.conn and not db.create_tables():
        print("cant save tables.Game worka without savimg.")
    
    # Получение имени пользователя
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game - Enter Username")
    
    username = ""
    input_active = True
    font = pygame.font.SysFont('Arial', 36)
    
    # Экран ввода имени пользователя
    while True:
        screen.fill(BLACK)
        
        draw_text(screen, "Enter your username:", 36, 
                  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, WHITE)
        
        # Поле ввода
        pygame.draw.rect(screen, WHITE, 
                         (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 40), 2)
        
        text_surface = font.render(username, True, WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 5))
        
        # Кнопка Start
        pygame.draw.rect(screen, GREEN, 
                         (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 60, 100, 40))
        draw_text(screen, "Start", 24, 
                  SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 70, BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (SCREEN_WIDTH // 2 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 50 and 
                    SCREEN_HEIGHT // 2 + 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 100):
                    break
        
        pygame.display.flip()
        
        # Проверка нажатия Enter или кнопки Start
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or (
            event.type == pygame.MOUSEBUTTONDOWN and 
            SCREEN_WIDTH // 2 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 50 and 
            SCREEN_HEIGHT // 2 + 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 100
        ):
            if username.strip():
                break
    
    username = username.strip() or "Player"
    
    # Проверка/создание пользователя
    user_id = None
    if db.conn:
        user = db.get_user(username)
        if user:
            user_id = user[0]
            print(f"Welcome back, {username}!")
            
            # Показываем лучшие результаты
            scores = db.get_user_scores(user_id)
            if scores:
                print("\nYour best scores:")
                for i, (score, level, game_time) in enumerate(scores, 1):
                    print(f"{i}. Score: {score}, Level: {level}, Time: {game_time//1000}s")
        else:
            user_id = db.create_user(username)
            if user_id:
                print(f"New user created: {username}")
            else:
                print("Failed to create user. Game will continue without saving scores.")
    
    # Основной игровой цикл
    while True:
        snake = Snake()
        food = Food()
        
        score = 0
        level = 1
        speed = 10
        game_start_time = pygame.time.get_ticks()
        paused = False
        game_over = False
        
        clock = pygame.time.Clock()
        
        running = True
        while running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused
                    
                    if not paused and not game_over:
                        if event.key == pygame.K_RIGHT:
                            snake.change_direction(1, 0)
                        elif event.key == pygame.K_LEFT:
                            snake.change_direction(-1, 0)
                        elif event.key == pygame.K_UP:
                            snake.change_direction(0, -1)
                        elif event.key == pygame.K_DOWN:
                            snake.change_direction(0, 1)
            
            if paused:
                # Отрисовка экрана паузы
                screen.fill(BLACK)
                snake.draw(screen)
                food.draw(screen)
                
                draw_text(screen, f"Score: {score}", 24, 10, 10)
                draw_text(screen, f"Level: {level}", 24, 10, 40)
                
                # Полупрозрачный прямоугольник для паузы
                s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                s.set_alpha(180)
                s.fill(BLACK)
                screen.blit(s, (0, 0))
                
                draw_text(screen, "PAUSED", 64, 
                          SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, WHITE)
                draw_text(screen, "Press P to continue", 24, 
                          SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 20, WHITE)
                
                pygame.display.flip()
                clock.tick(FPS)
                continue
            
            if game_over:
                game_time = pygame.time.get_ticks() - game_start_time
                result = show_game_over(screen, score, level, game_time)
                
                if result == "restart":
                    break
                elif result == "quit":
                    running = False
                    break
            
            # Игровая логика
            snake.move()
            
            # Проверка столкновений
            if snake.check_collision():
                game_over = True
                game_time = pygame.time.get_ticks() - game_start_time
                
                # Сохраняем результат
                if db.conn and user_id:
                    db.save_score(user_id, score, level, game_time)
                
                continue
            
            # Проверка съедения еды
            if snake.body[0] == food.pos:
                score += food.weight
                
                # Повышение уровня каждые 10 очков
                if score // 10 > (score - food.weight) // 10:
                    level += 1
                    speed += 1
                
                snake.grow = True
                food.randomize(snake.body)
            
            # Проверка времени жизни еды
            if food.expired():
                food.randomize(snake.body)
            
            # Отрисовка
            screen.fill(BLACK)
            
            # Отрисовка сетки (опционально)
            for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
                pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))
            
            snake.draw(screen)
            food.draw(screen)
            
            draw_text(screen, f"Score: {score}", 24, 10, 10)
            draw_text(screen, f"Level: {level}", 24, 10, 40)
            draw_text(screen, f"Player: {username}", 24, 10, 70)
            
            pygame.display.flip()
            clock.tick(speed)
        
        if not running:
            break
    
    db.close()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()