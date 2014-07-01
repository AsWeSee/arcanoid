import pygame
import sys
from pygame.locals import *
from scenes import *

class Game():
    RESOLUTION = (800, 600) # 90*5 and 90*8, 5 and 8 -> fibo numbers.
    def __init__(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode(self.RESOLUTION)
        self.action_scene = Scene()

    def Loop(self):
        while 1:
            self.action_scene.draw(self.surface)
            result = self.action_scene.handleActions()
            if result == None: #если действий не было вернётся None
                continue       #иначе 0 если выход
            elif result == 'battle': # ключи сцен если нужно поменять сцену
                self.action_scene.close()
                pass
            elif not result:
                print("Ключ смены сцены =",result)
                print('Выход')
                pygame.quit()
                break
        print(self.action_scene)

if __name__ == '__main__':
    MAIN = Game()
    print(MAIN.RESOLUTION)
    MAIN.Loop()
    
