import pygame
from pygame.locals import *
#Все обьекты принажлежат какой либо одной сцене
#Это может быть боевая сцена или меню с кнопками.
class Scene():

    def __init__(self):
        self.image2 = pygame.image.load('image2.png')
        self.background = pygame.image.load('background.png')

    def draw(self, surface):
        surface.blit(self.background, (0,0))
        y = min(pygame.mouse.get_pos()[0],800-64)
        
        surface.blit(self.image2, (y,570))
        pygame.display.flip()
    def handleActions(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0
    def close(self):
        pass #Выгружаем картинки
## Однако, возможно что загрузить все данные при старте приложения выгоднее чем
##    каждый раз загружать и чистить 
## Тогда удаляем массивы данных явно. Это безопаснее чем удалять ссылки и ждать
##    сборщика мусора    
