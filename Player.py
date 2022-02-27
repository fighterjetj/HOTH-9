import pygame
import Actor

BASE_UNIT = 16
Y_MIN = 0
Y_MAX = 512+128
X_MAX = 2048-64
X_MIN = 16
class Player(Actor.Actor):
    def __init__(self, cords, image_path, size, ground, gravity_on):
        Actor.Actor.__init__(self, cords, image_path, size)
        self.ABOVE_GROUND = BASE_UNIT
        self.face_right = True
        self.gravity = gravity_on
        self.ground_y = self.y
        self.jump_time = 0
        self.ground = ground
        self.y_vel = -1

    def on_ground(self):
        adj_x = int(self.x/BASE_UNIT)
        adj_y = int(self.y/BASE_UNIT)
        adj_size = (int(self.size[0]/BASE_UNIT), int(self.size[1]/BASE_UNIT))
        for x in range(adj_size[0]):
            #print(f"Checking at {adj_x, adj_y}")
            if self.ground.is_ground(adj_x, adj_y):
                return True
        return False

    def render(self, window, dimensions):
        height, width = dimensions
        cords = (int((width-self.size[0])/2), height-self.size[1]-self.ABOVE_GROUND)
        window.blit(self.image, cords)
        if (self.gravity):
            if (self.on_ground()):
                #print("ON GROUND")
                self.jump_time = 0
            else:
                self.y -= BASE_UNIT*self.y_vel
            if (self.y_vel >= 0):
                self.y_vel -= 1
        if self.y < Y_MIN:
            self.y = Y_MAX
        elif self.y > Y_MAX:
            self.y = Y_MIN
        if self.x < X_MIN:
            self.x = X_MAX
        elif self.x > X_MAX:
            self.x = X_MIN

    def handle_keys(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            if self.face_right:
                self.face_right = False
                self.image = pygame.transform.flip(self.image, True, False)
            self.x -= BASE_UNIT
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            if not self.face_right:
                self.face_right = True
                self.image = pygame.transform.flip(self.image, True, False)
            self.x += BASE_UNIT
        elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            if self.gravity:
                if self.on_ground():
                    #print("Jumping!")
                    self.y_vel = 5
                    self.y -= BASE_UNIT
            else:
                self.y -= BASE_UNIT
        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            if not self.gravity:
                self.y += BASE_UNIT
