import pygame
import os
from pygame.math import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '0'

class Unit():
    def __init__(self, state, position, tile):
        self.state = state
        self.position = position
        self.tile = tile
    def move(self, moveVector):
        raise NotImplementedError()

class Tank(Unit):
    def move(self, moveVector):
        newPos = self.position + moveVector
        if newPos.x < 0 or newPos.x >= self.state.worldSize.x \
        or newPos.y < 0 or newPos.y >= self.state.worldSize.y:
            return
        for unit in self.state.units:
            if newPos == unit.position:
                return
        self.position = newPos

class Tower(Unit):
    def move(self, moveVector):
        pass

class GameState:
    def __init__(self):
        self.worldSize = Vector2(16, 10)
        self.units = [
            Tank(self, Vector2(5, 4), Vector2(1,0)),
            Tower(self, Vector2(10, 3), Vector2(0,1)),
            Tower(self, Vector2(10, 5), Vector2(0,1))
        ]
        self.ground = [
    [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
    [ Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(6,4), Vector2(7,2), Vector2(7,2)],
    [ Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(6,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(6,1), Vector2(5,1)],
    [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(7,1)],
    [ Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,5), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(8,5), Vector2(5,1), Vector2(5,1)],
    [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(7,1)],
    [ Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(7,1), Vector2(5,1)],
    [ Vector2(5,1), Vector2(5,1), Vector2(6,4), Vector2(7,2), Vector2(7,2), Vector2(8,4), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1)],
    [ Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(7,4), Vector2(7,2), Vector2(7,2)],
    [ Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)]
]

    def update(self, moveTankCommand):
        for unit in self.units:
            unit.move(moveTankCommand)

class UserInterface:
    #properties
    @property
    def worldWidth(self):
        return int(self.gameState.worldSize.x)
    @property
    def worldHeight(self):
        return int(self.gameState.worldSize.y)
    @property
    def cellWidth(self):
        return int(self.cellSize.x)
    @property
    def cellHeight(self):
        return int(self.cellSize.y)

    #rest of the class
    def __init__(self):
        pygame.init()

        self.gameState = GameState()
        self.cellSize = Vector2(64, 64)
        self.unitsTexture = pygame.image.load("units.png")
        self.groundTexture = pygame.image.load("background.png")

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
    
    def renderGround(self, position, tile):
        #location on screen
        spritePoint = position.elementwise() * self.cellSize

        #texture
        texturePoint = tile.elementwise() * self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.groundTexture, spritePoint, textureRect)

    def renderUnit(self, unit):
        #location on screen
        spritePoint = unit.position.elementwise() * self.cellSize

        #unit texture
        texturePoint = unit.tile.elementwise() * self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.unitsTexture, spritePoint, textureRect)

        #weapon texture
        texturePoint = Vector2(0,6).elementwise() * self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.unitsTexture, spritePoint, textureRect)

    def render(self):
        self.window.fill((0, 0, 0))
        for y in range(self.worldHeight):
            for x in range(self.worldWidth):
                self.renderGround(Vector2(x,y),self.gameState.ground[y][x])
        for unit in self.gameState.units:
            self.renderUnit(unit)
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

ui = UserInterface()
ui.run()
