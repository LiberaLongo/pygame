import pygame
import os
from pygame.math import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '0'

class GameState:
    def __init__(self):
        self.worldSize = Vector2(16, 10)
        self.tankPos = Vector2(5, 4)
        self.tower1Pos = Vector2(10, 3)
        self.tower2Pos = Vector2(10, 5)

    def update(self, moveTankCommand):
        newTankPos = self.tankPos + moveTankCommand
        if newTankPos.x >= 0 and newTankPos.x < self.worldSize.x \
        and newTankPos.y >=0 and newTankPos.y < self.worldSize.y \
        and newTankPos != self.tower1Pos and newTankPos != self.tower2Pos:
            self.tankPos = newTankPos

class UserInterface:
    def __init__(self):
        pygame.init()

        self.gameState = GameState()
        self.cellSize = Vector2(64, 64)
        self.unitsTexture = pygame.image.load("units.png")

        windowSize = self.gameState.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))

        pygame.display.set_caption("discover python & patterns - https://www.patternsgameprog.com")
#       pygame.display.set_icon(pygame.image.load("icon.png"))
        
        self.moveTankCommand = Vector2(0,0)
        self.clock = pygame.time.Clock()
        self.running = True

    def processInput(self):
        self.moveTankCommand.x = 0
        self.moveTankCommand.y = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moveTankCommand.x += 1 
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moveTankCommand.x -= 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.moveTankCommand.y += 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.moveTankCommand.y -= 1
    
    def update(self):
        self.gameState.update(self.moveTankCommand)

    def render(self):
        self.window.fill((0, 0, 0))
#tank        
        spritePoint = self.gameState.tankPos.elementwise() * self.cellSize
        texturePoint = Vector2(1,0).elementwise() * self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)
#1st tower     
        spritePoint = self.gameState.tower1Pos.elementwise() * self.cellSize
        texturePoint = Vector2(0,6).elementwise() * self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)
#2nd tower
        spritePoint = self.gameState.tower2Pos.elementwise() * self.cellSize
        texturePoint = Vector2(0,6).elementwise() * self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)
        
        
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

ui = UserInterface()
ui.run()
