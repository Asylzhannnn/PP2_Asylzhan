import pygame
import random
import time

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load(r"C:\Users\Acer\Desktop\Python\AnimatedStreet.png")
player_img = pygame.image.load(r"C:\Users\Acer\Desktop\Python\Player.png")
enemy_img = pygame.image.load(r"C:\Users\Acer\Desktop\Python\Enemy.png")
coin_img = pygame.image.load(r"C:\Users\Acer\Desktop\Python\coin.png")

#music
pygame.mixer.music.load(r"C:\Users\Acer\Desktop\Python\background.wav")
crash_sound = pygame.mixer.Sound(r"C:\Users\Acer\Desktop\Python\crash.wav")
pygame.mixer.music.play(-1)

#shrifts
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "red")
coin_count_font = pygame.font.SysFont("Verdana", 20)

PLAYER_SPEED = 5
ENEMY_SPEED = 4
COIN_SPEED = 2
COIN_COUNT_TO_INCREASE_SPEED = 5  #every five coins increases speed
coin_count = 0

def increase_enemy_speed():
    for enemy in enemy_sprites:
        enemy.speed += 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        self.rect.clamp_ip(screen.get_rect())#невыходит за границы

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.speed = ENEMY_SPEED
        self.generate_random_position()
    
    def move(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.generate_random_position()
    
    def generate_random_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -self.rect.h

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.generate_random_coin()
    
    def move(self):
        self.rect.y += COIN_SPEED
        if self.rect.top > HEIGHT:
            self.generate_random_coin()
    
    def generate_random_coin(self):
        size = random.randint(30, 60)  #coins with differnt sizes
        self.image = pygame.transform.scale(coin_img, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -self.rect.h

#creating the oblects
player = Player()
enemies = [Enemy() for _ in range(1)]  #initial enemy
coin = Coin()

all_sprites = pygame.sprite.Group(player, *enemies, coin)
enemy_sprites = pygame.sprite.Group(*enemies)
coin_sprites = pygame.sprite.Group(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    #moving the objects
    player.move()
    for enemy in enemy_sprites:
        enemy.move()
    coin.move()
    
    #Отрисовкаа
    all_sprites.draw(screen)
    
    if pygame.sprite.spritecollideany(player, coin_sprites):  #чек столкновения с монетой
        coin_count += 1
        coin.generate_random_coin()
        if coin_count % COIN_COUNT_TO_INCREASE_SPEED == 0:
            increase_enemy_speed()
            new_enemy = Enemy()
            enemy_sprites.add(new_enemy)
            all_sprites.add(new_enemy)
    
    if pygame.sprite.spritecollideany(player, enemy_sprites):      #чек столкновения с врагом
        crash_sound.play()
        time.sleep(1)
        screen.fill("black")
        screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        time.sleep(2)
        running = False
    
    #счет
    counting = coin_count_font.render(f"Coins: {coin_count}", True, "black")
    screen.blit(counting, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
