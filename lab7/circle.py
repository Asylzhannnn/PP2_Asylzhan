import pygame
pygame.init()
pos1 = 75
pos2 = 75
black = (255,0,0)
screen = pygame.display.set_mode((150, 150))
pygame.draw.circle(screen, black, (pos1, pos2), 25)
screen.fill((255,255,255))
done = False
def down():
    global pos1,pos2
    if pos2 + 25 <= 125:
        pos2+=20
def left():
    global pos1,pos2
    if pos1 - 20 >= 25:
        pos1-=20
def up():
    global pos1,pos2
    if pos2 - 25 >= 25:
        pos2-=20
def right():
    global pos1,pos2
    if pos1 + 20 <= 125:
        pos1+=20
#pos1 = width
#pos2 = height

while not done:
    pygame.draw.circle(screen, black, (pos1, pos2), 25)
    screen.fill((255,255,255))
    pygame.draw.circle(screen, black, (pos1, pos2), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  
                    up()
                elif event.key == pygame.K_DOWN:
                    down()
                elif event.key == pygame.K_LEFT:
                    left()  
                elif event.key == pygame.K_RIGHT:
                    right()
        
    pygame.display.flip()
pygame.quit()