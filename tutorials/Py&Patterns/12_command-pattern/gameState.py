import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '0'

class GameState:
    def __init__(self):
        self.x = 120
        self.y = 120
    def update(self, moveCommandX, moveCommandY):
        self.x += moveCommandX
        self.y += moveCommandY

class UserInterface:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Discover python & paatterns = https://www.paternsgameprog.com")
        pygame.display.set_icon(pygame.image.load("icon.png"))
        self.clock = pygame.time.Clock()
        self.running = True
        self.gameState = GameState()

    def processInput(self):
        self.moveCommandX = 0
        self.moveCommandY = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moveCommandX += 8
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moveCommandX -= 8
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.moveCommandY += 8
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.moveCommandY -= 8

    def update(self):
        self.gameState.update(self.moveCommandX, self.moveCommandY)

    def render(self):
        self.window.fill((0, 0, 0))
        color = (255, 0, 255)
        x = self.gameState.x
        y = self.gameState.y
        rect = (x, y, 400, 240)
        pygame.draw.rect(self.window, color, rect)
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

ui = UserInterface()
ui.run()
