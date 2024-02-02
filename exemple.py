import pygame

long = 800
haut = 600

surf = pygame.display.set_mode((long,haut))
run = True
clock = pygame.time.Clock()
l, h = long//2, haut//2
lsnake = 10
hsnake = 10
direction = None
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                direction = "down"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "right"
    if direction == "up":
        h -= 1
    if direction == "down":
        h += 1
    if direction == "right":
        l += 1
    if direction == "left":
        l -= 1
    if h < 0:
        print("Game Over")
        l, h = long // 2, haut // 2
    if h > haut - hsnake:
        print("Game Over")
        l, h = long // 2, haut // 2
    if l > long - lsnake:
        print("Game Over")
        l, h = long // 2, haut // 2
    if l < 0:
        print("Game Over")
        l, h = long // 2, haut // 2

    clock.tick(240)
    surf.fill((0,0,0))
    pygame.draw.rect(surf, (255,255,255), (l,h,lsnake,hsnake))
    pygame.display.flip()

pygame.quit()