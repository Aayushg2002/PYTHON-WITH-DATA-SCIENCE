import pgzrun
box = Rect((50,50),(150,100))
box2 = Rect((400,50) ,(100,100))
def draw():
    screen.fill('black')
    screen.draw.filled_rect(box, 'yellow')
    screen.draw.filled_rect(box2,'red')

def update():
    pass

pgzrun.go()