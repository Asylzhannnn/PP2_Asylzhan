import pygame 
import time
import datetime
pygame.init()

screen = pygame.display.set_mode((800, 600)) #size of window
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey clock") #name of window

leftarm = pygame.image.load("sec_hand.png")
rightarm = pygame.image.load("min_hand.png")
mainclock = pygame.transform.scale(pygame.image.load("clock.png"), (800, 600))

rightarm = pygame.transform.scale(rightarm, (800, 700))  # Минутная стрелка (правая рука)
leftarm = pygame.transform.scale(leftarm, (800, 700))  # Секундная стрелка (левая рука)

CENTER = (400, 300)

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
   
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second
    
    angle_minute = ((minute * 0) + 60) - minute * 6   #Вычисляем углы поворота
    angle_second = -(second * 6)  
    
    screen.blit(mainclock, (0, 0))#Отображаем фон
    
    rotated_rightarm = pygame.transform.rotate(rightarm, angle_minute)#Вращаем и отображаем минутную руку (правую)
    rightarmrect = rotated_rightarm.get_rect(center=CENTER)
    screen.blit(rotated_rightarm, rightarmrect)
    
    rotated_leftarm = pygame.transform.rotate(leftarm, angle_second) #Вращаем и отображаем секундную руку (левую)
    leftarmrect = rotated_leftarm.get_rect(center=CENTER)
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip()  # Обновляемэкран
    clock.tick(60)#FPS
    
pygame.quit()