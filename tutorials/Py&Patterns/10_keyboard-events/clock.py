import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Discover python & paatterns = https://www.paternsgameprog.com")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()

x = 120
y = 120
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 8
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 8
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 8
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 8

    window.fill((0, 0, 0))
    color = (255, 0, 255)
    rect = (x, y, 400, 240)
    pygame.draw.rect(window, color, rect)
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()

