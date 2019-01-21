pipe = []
global score

score = 0


from Bird import Bird
from Pipe import Pipe


def setup():
    size(1200, 800)
    
    global bird, speed, f, pipe_gap, pipe_height, pipe_width, max_height, min_height, gap, start_gap
    
    bird = Bird(width / 4, height / 2, 1, 40)
    speed = 5
    fill(255, 0, 0)
    textAlign(CENTER)
    f = createFont("Arial", 16, True)
    start_gap = width
    
    gap = 150
    pipe_height = 800
    pipe_width = 100
    pipe_gap = pipe_height + gap
    
    gap_range = 100
    max_height = height / (pipe_height / 100) - gap_range - 100
    min_height = height / (pipe_height / 100) + gap_range

    
    pipe.append(Pipe(width / 3 + start_gap, random(max_height, min_height), speed, pipe_width, pipe_height, pipe_gap))
    pipe.append(Pipe(2 * width / 3 + start_gap + 50, random(max_height, min_height), speed, pipe_width, pipe_height, pipe_gap))
    pipe.append(Pipe(width + start_gap + 100, random(max_height, min_height), speed, pipe_width, pipe_height, pipe_gap))


def draw():
    background(0, 50, 150)
    global score
    
    player_score = score
    

    if (bird.y >= height + 40):
        bird.dead = True
        for p in pipe:
            p.dead = True
    
    elif (bird.y <= 0):
        bird.y = 10
        bird.speed = 0
    
    
    bird.show()
    bird.update()
    

    for p in pipe:
        if (p.x <= -40):
            p.reset(max_height, min_height)
            p.got_point = False
        
        
        if not(bird.y - bird.r / 2 >= p.y + p.h * 0.5 and bird.y + bird.r / 2 <= p.y + p.h * 0.5 + gap) and ((bird.x + bird.r / 2 >= p.x - p.w * 0.5 and bird.x - bird.r / 2 <= p.x + p.w * 0.5 and bird.y + bird.r / 2 <= p.y - p.h * 0.5) or (bird.x + bird.r / 2 >= p.x - p.w * 0.5 and bird.x - bird.r / 2 <= p.x + p.w * 0.5 and bird.y + bird.r / 2 <= p.y + p.h * 0.5 + p.gap)):
            bird.dead = True
            for p in pipe:
                p.dead = True
        
        
        p.scroll()
        p.show()
        p.update(bird, player_score)
        
        player_score += p.score
        
        
        if (bird.dead):
            fill(255, 0, 0)
            textFont(f, 100)                      
            text("GAME OVER", width / 2, height / 2)
            textFont(f, 50)
            text("Press R to restart", width / 2, height / 2 + 150)
    
    textFont(f, 50)
    fill(0, 255, 0)
    text(player_score, width / 2, 100)


def keyPressed():
    if(key == ' '):
        bird.speed -= 10
    
    elif(key == 'r'):
        bird.reset()
        score = 0
        
        for p in pipe:
            pipe.remove(p)
        
        pipe.append(Pipe(width / 3 + start_gap, random(max_height, min_height), speed, pipe_width, pipe_height, pipe_gap))
        pipe.append(Pipe(2 * width / 3 + start_gap + 50, random(max_height, min_height), speed, pipe_width, pipe_height, pipe_gap))
        pipe.append(Pipe(width + start_gap + 100, random(max_height, min_height), speed, pipe_width, pipe_height, pipe_gap))
