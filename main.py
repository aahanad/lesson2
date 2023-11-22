import pgzrun
WIDTH=500
HEIGHT=600
def draw ():
    screen.fill("teal")
    rectangle=Rect(200,350,180,100)
    #screen.draw.rect(rectangle,"violet")
    screen.draw.filled_rect(rectangle,"violet")
    screen.draw.filled_circle((100,250),89,"light coral")
pgzrun.go()    
    