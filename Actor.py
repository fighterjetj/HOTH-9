import pygame

HEIGHT,WIDTH = 512,512

class Actor:
    def __init__(self, cords, image_path, size, function=None):
        self.function = function
        self.x, self.y = cords
        self.image_path = image_path
        self.size = size
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)

    def render(self, window, player, dimensions):
        width, height = dimensions
        player_size = player.get_size()
        p_x = player.get_x()
        p_y = player.get_y()
        width_offset = p_x-int((width-player_size[0])/2)
        height_offset = p_y-height+2*player.ABOVE_GROUND
        relative_x = self.x - width_offset
        relative_y = self.y - height_offset
        #print (f"The upper right corner of the screen is {width_offset, height_offset}")
        window.blit(self.image, (relative_x, relative_y))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size
        
    def handle_event(self, event):
        if self.function:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.function()

    def clicked(self):
        if self.function:
            self.function()
