import pygame
import Actor
import Player
import level_loader
import value_handler
import ground_storage


FPS = 30
dimensions = (512, 512)
WIDTH, HEIGHT = dimensions
BLOCK_PATH = "Images/block.png"
PLAYER_PATH = "Images/amongus.png"
LEVEL_PATH = "Level.txt"
BASE_UNIT = 16
BLOCK_BUILDING = False
THEME_SONG = "Audio/theme_song.mp3"


# Making the window
window = pygame.display.set_mode((WIDTH,HEIGHT))

# Setting the window name
pygame.display.set_caption("HOTH 9 Game")

# Initializing the window
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(THEME_SONG)
  
# Setting the volume
pygame.mixer.music.set_volume(1.0)
  
# Start playing the song
pygame.mixer.music.play()

# Makes a key for loading the images
val_handler = value_handler.Value_Handler()
val_handler.add_val('#', "BLOCK")
val_handler.add_val(' ', "EMPTY")
val_handler.add_val('@', "PLAYER")
val_handler.add_val('H', "HOUSE")
val_handler.add_val('1', "G1")
val_handler.add_val('2', "G2")
val_handler.add_val('3', "G3")
val_handler.add_val('T', "TREE")
# List for storing the solid ground
# Dictionary of objects to render
to_render = {}
# Loads the level
solid_ground = level_loader.load_level(to_render, LEVEL_PATH, val_handler)
# Makes a clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,24)
text = font.render("Fossil Fuels are the imposter????    SUStainability ISN'T SUS", True, pygame.Color("Purple"))
running = True
player = to_render["PLAYER"]
while running:
    # Makes the game update at the FPS
    clock.tick(FPS)
    # Gets where the mouse clicked
    mouse_clicked = pygame.mouse.get_pressed()[0]
    if mouse_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = player.get_x() + int(mouse_x - WIDTH/2)+BASE_UNIT
        mouse_y = player.get_y() + (mouse_y - HEIGHT + BASE_UNIT) + BASE_UNIT
        #print(f"WE CLICKED {mouse_x, mouse_y}")
        for actor in to_render["LAYER_1"]:
            act_x = actor.get_x()
            act_y = actor.get_y()
            act_size = actor.get_size()
            #print(f"HAS A SIZE OF {act_size} AND COORDINATES OF {act_x, act_y}")
            if (act_x < mouse_x and mouse_x < act_x + act_size[0]) and (act_y < mouse_y and mouse_y < act_y + act_size[1]):
                actor.clicked()
        mouse_x = int(mouse_x/BASE_UNIT)
        mouse_y = int(mouse_y/BASE_UNIT)
        if (not solid_ground.is_ground(mouse_x, mouse_y) and BLOCK_BUILDING):
            print(f"ADDING BLOCK AT {mouse_x, mouse_y}")
            size = (16,16)
            to_render["LAYER_0"].append(Actor.Actor(((mouse_x+1)*16, (mouse_y+1)*16), BLOCK_PATH, size))
            solid_ground.add_ground(mouse_x, mouse_y)
        
    events = pygame.event.get()
    # Goes through the events and passes the events to each object that needs to check the events
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
    pressed_keys = pygame.key.get_pressed()
    player.handle_keys(pressed_keys)
    window.fill(pygame.Color("Light Blue"))
    for actor in to_render["LAYER_0"]:
        actor.render(window, player, dimensions)
    for actor in to_render["LAYER_1"]:
        actor.render(window, player, dimensions)
    window.blit(text, (0, int(HEIGHT/2)))
    player.render(window, dimensions)
    pygame.display.update()
pygame.quit()
