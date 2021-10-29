import pygame

class Ball:
   # pass
   #class variables
    RADIUS= 10

    def __init__(self, x, y, vx, vy, screen, bcolor, bgcolor, CONSTS):
        #instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.bcolor = bcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS
        
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    
    def update(self):
        self.show(self.bgcolor)
        px = self.x + self.vx
        py = self.y + self.vy
        #Check if im colliding (wall position):
            #flip the velocity
        #left wall
        if px < (self.CONSTS.BORDER + self.RADIUS):
            self.vx = -self.vx
        #top wall
        if py < (self.CONSTS.BORDER + self.RADIUS):
            self.vy = -self.vy
        #bottom wall
        if py > (self.CONSTS.HEIGHT-self.CONSTS.BORDER - self.RADIUS):
            self.vy = -self.vy
        

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.bcolor)