import pygame
import os

pygame.init()

# Загружаем музыку из папки
playlist = []
music_folder = r"C:\Users\Acer\Desktop\Python\playlist"

if os.path.exists(music_folder):  # Проверяем, существует ли папка
    allmusic = os.listdir(music_folder)
    for song in allmusic:
        if song.endswith(".mp3"):
            playlist.append(os.path.join(music_folder, song))

if not playlist:
    print("Нет доступных файлов .mp3 в указанной папке!")
    pygame.quit()
    exit()

# Создаем окно
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sade")
clock = pygame.time.Clock()

# Загружаем изображения
background = pygame.image.load(os.path.join("music-elements", "background.png"))
bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

playb = pygame.transform.scale(pygame.image.load(os.path.join("music-elements", "play.png")), (70, 70))
pausb = pygame.transform.scale(pygame.image.load(os.path.join("music-elements", "pause.png")), (70, 70))
nextb = pygame.transform.scale(pygame.image.load(os.path.join("music-elements", "next.png")), (70, 70))
prevb = pygame.transform.scale(pygame.image.load(os.path.join("music-elements", "back.png")), (75, 75))

# Инициализируем переменные
index = 0
aplay = False

# Загружаем и запускаем первый трек
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()
aplay = True  

run = True

while run:
    screen.fill((255, 255, 255))  # Очищаем экран

    # Отображаем фон и кнопки
    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(nextb, (460, 587))
    screen.blit(prevb, (273, 585))

    if aplay:
        screen.blit(pausb, (370, 590))
    else:
        screen.blit(playb, (370, 590))

    # Отображаем название трека
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(text2, (365, 520))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Нажатие на кнопку Play/Pause
            if 370 <= x <= 440 and 590 <= y <= 660:
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay

            # Нажатие на кнопку Next
            if 460 <= x <= 530 and 587 <= y <= 657:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True  

            # Нажатие на кнопку Previous
            if 273 <= x <= 348 and 585 <= y <= 660:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пауза/возобновление
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay

            if event.key == pygame.K_RIGHT:  # Следующий трек
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True  

            if event.key == pygame.K_LEFT:  # Предыдущий трек
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True  

            if event.key == pygame.K_s:  # Остановить воспроизведение
                pygame.mixer.music.stop()
                aplay = False  

    clock.tick(24)
    pygame.display.update()
  