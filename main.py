import pygame

FPS = 60
WIDTH,HEIGHT=600,600
# Making the window
window = pygame.display.set_mode((WIDTH,HEIGHT))

# Setting the window name
pygame.display.set_caption("HOTH 9 Game")
# Initializing the window
pygame.init()
# Makes a clock
clock = pygame.time.Clock()
imposterX = 100
imposterY = 100
imposter = pygame.image.load('Images/amongus.png')
running = True
while running:
    # Makes the game update at the FPS
    clock.tick(FPS)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    events = pygame.event.get()
    # Goes through the events and passes the events to each object that needs to check the events
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                imposterX -= 10
            elif event.key == pygame.K_RIGHT:
                imposterX += 10
            elif event.key == pygame.K_UP:
                imposterY -= 10
            elif event.key == pygame.K_DOWN:
                imposterY += 10
    window.fill(pygame.Color("Light Blue"))
    window.blit(imposter, (imposterX, imposterY))
    pygame.display.update()
pygame.quit()
