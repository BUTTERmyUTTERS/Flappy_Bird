class Bird(object):
    def __init__(self, x, y, speed, r):
        self.x = x
        self.y = y
        self.angle = 0
        self.acc = 0.25
        self.speed = 0
        self.dead = False
        self.r = r
    
    
    def jump(self, vel):
        self.y = lerp(self.y, self.y - vel, 0.1)
    
    
    def show(self):
        if not(self.dead):
            fill(255)
            ellipseMode(CENTER)
            ellipse(self.x, self.y, self.r, self.r)
    
    
    def update(self):
        if not(self.dead):
            self.y += self.speed
            self.speed += self.acc
            self.speed = constrain( self.speed, -10, 10)
    
    
    def reset(self):
        self.speed = 0
        self.y = height / 2
        self.dead = False
        
