import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

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

pygame.quit()

