import pygame
import Actor
import Player
import ground_storage

BLOCK_PATH = "Images/block.png"
PLAYER_PATH = "Images/amongus.png"
G1_PATH = "Images/game1.png"
G2_PATH = "Images/game2.png"
G3_PATH = "Images/game3.png"
HOUSE_PATH = "Images/house.png"
TREE_PATH = "Images/tree.png"


def game_1():
    print("G1")
def game_2():
    print("G2")
def game_3():
    print("G3")

def load_level(all_actors, path, value_handler):
    all_actors["LAYER_0"] = []
    all_actors["LAYER_1"] = []
    with open (path) as level:
        lines = level.readlines()
    height = len(lines)
    width = len(lines[0])
    solid_ground = ground_storage.Ground(width, height)
    for y_val, line in enumerate(lines):
        for x_val, char in enumerate(line):
            cords = ((x_val)*16, (y_val+1)*16)
            #print(f"Adding character to {cords}")
            to_make = value_handler.get_val(char)
            if to_make == "BLOCK":
                size = (16,16)
                solid_ground.add_ground(x_val,y_val)
                all_actors["LAYER_0"].append(Actor.Actor(cords, BLOCK_PATH, size))
            elif to_make == "G1":
                size = (128, 128)
                all_actors["LAYER_1"].append(Actor.Actor((cords[0], cords[1]-(size[1]-16)), G1_PATH, size, game_1))
            elif to_make == "G2":
                print(f"Game 2 is at {cords[0], cords[1]-(size[1]-16)}")
                size = (128, 128)
                all_actors["LAYER_1"].append(Actor.Actor((cords[0], cords[1]-(size[1]-16)), G2_PATH, size, game_2))
            elif to_make == "G3":
                size = (128, 128)
                all_actors["LAYER_1"].append(Actor.Actor((cords[0], cords[1]-(size[1]-16)), G3_PATH, size, game_3))
            elif to_make == "HOUSE":
                size = (128, 128)
                all_actors["LAYER_1"].append(Actor.Actor((cords[0], cords[1]-(size[1]-16)), HOUSE_PATH, size))
            elif to_make == "TREE":
                size = (64, 128)
                all_actors["LAYER_1"].append(Actor.Actor((cords[0], cords[1]-(size[1]-16)), TREE_PATH, size))
            elif to_make == "PLAYER":
                size = (48,48)
                all_actors["PLAYER"] = Player.Player(cords, PLAYER_PATH, size, solid_ground, True)
                
    return solid_ground

