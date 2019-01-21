class Pipe(object):
    def __init__(self, x, y, speed, w, h, gap):
        self.x = x
        self.y = y
        self.speed = speed
        self.w = w
        self.h = h
        self.gap = gap
        self.dead = False
        self.got_point = False
        self.score = 0
    
    
    def scroll(self):
        if not(self.dead):
            self.x = lerp(self.x, self.x - self.speed, 0.1)
    
    
    def show(self):
        if not(self.dead):
            rectMode(CENTER)
            fill(255)
            rect(self.x, self.y, self.w, self.h)
            rect(self.x, self.y + self.gap, self.w, self.h)
    
    
    def update(self, bird, score):
        if not(self.dead):
            self.x -= self.speed
        
        if (self.got_point == False):
            if (self.x < bird.x):
                self.score += 1
                self.got_point = True
    
    
    def reset(self, maxH, minH):
        self.x = width + self.w
        self.y = random(maxH, minH)
        self.dead = False
