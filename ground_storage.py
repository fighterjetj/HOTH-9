import pygame

class Ground:
    def __init__(self, width, length):
        base = [False]*width
        self.ground = []
        for i in range(length):
            self.ground.append(base[:])
        self.num_true = 0

    def add_ground(self, x, y):
        #print("Adding a true value!")
        (self.ground)[y][x] = True
        self.num_true += 1


    def is_ground(self, x, y):
        #print(self.ground)
        #print(f"The ground dimensions are {len(self.ground), len(self.ground[0])}")
        try:
            return self.ground[y][x]
        except IndexError:
            return False

    def draw_ground_spots(self):
        for row in self.ground:
            for col in row:
                if col:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
    
    def num_ground_spots(self):
        i = 0
        for row in self.ground:
            for col in row:
                if col:
                    i += 1
        return i
        
